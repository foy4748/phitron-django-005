from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import UpdateAPIView, RetrieveAPIView

from people.models import People
from people.serializers import (
    BalanceCheckSerializer,
    BalanceDepositeSerializer,
    LoginSerializer,
    RegistrationSerializer,
    UserListSerializer,
)

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator

# from django.utils.http import urlsafe_base64_encode  # , urlsafe_base64_decode
from rest_framework.permissions import IsAuthenticated
from django.utils.encoding import force_bytes

# from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

# from rest_framework.authtoken.models import Token

# for sending email
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string

# from django.shortcuts import redirect


class UserRegistrationApiView(APIView):
    serializer_class = RegistrationSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)

            # Email Related
            # confirm_link = f"http://127.0.0.1:3000/patient/active/{uid}/{token}"
            # email_subject = "Confirm Your Email"
            # email_body = render_to_string(
            #     "confirm_email.html", {"confirm_link": confirm_link}
            # )

            # email = EmailMultiAlternatives(email_subject, "", to=[user.email])
            # email.attach_alternative(email_body, "text/html")
            # email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)


class UserLoginView(APIView):
    # serializer_class = LoginSerializer)

    def post(self, request):
        s = LoginSerializer(data=request.data)
        user = None
        if s.is_valid():
            current_username = s.validated_data.get("username", None)
            current_password = s.validated_data.get("password")
            user = authenticate(
                request, username=current_username, password=current_password
            )

        else:
            return Response(s.errors)

        if user is not None:
            login(request, user)
            token, is_token_was_created = Token.objects.get_or_create(user=user)

            h = dict()
            h["Authorization"] = f"Token {token.key}"
            h["Content-Type"] = "application/json"
            return Response(
                {
                    "success": True,
                    "token_was_created": is_token_was_created,
                    "message": "User LoggedIn",
                    "token": token.key,
                    "user_id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "image_url": user.people_info.image_url,
                    "phone_no": user.people_info.phone_no,
                },
                headers=h,
            )
        else:
            return Response({"success": False, "message": "Authentication Failed"})


class BalanceDepositeView(UpdateAPIView):
    serializer_class = BalanceDepositeSerializer
    permission_classes = [IsAuthenticated]
    queryset = People.objects.all()

    def get_object(self):
        user_id = self.request.user.id
        return People.objects.get(basic_info__id=user_id)


class BalanceCheckView(RetrieveAPIView):
    serializer_class = BalanceCheckSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return People.objects.get(basic_info=self.request.user)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def test_protected_route(_):
    return Response({"success": True, "message": "User is authenticated"})
