from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from people.models import People
from people.serializers import (
    BalanceCheckSerializer,
    BalanceDepositeSerializer,
    ChangePasswordSerializer,
    LoginSerializer,
    RegistrationSerializer,
    ResetPasswordPayloadSerializer,
    ResetPasswordSerializer,
    UserListSerializer,
)

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator

# from django.utils.http import urlsafe_base64_encode  # , urlsafe_base64_decode
from rest_framework.permissions import IsAuthenticated
from django.utils.encoding import force_bytes

# from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from utils.send_email import user_activation_email

# from rest_framework.authtoken.models import Token

# for sending email
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string

# from django.shortcuts import redirect


class UserRegistrationApiView(APIView):
    serializer_class = RegistrationSerializer

    def get(self):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            # print(user)
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

            user_activation_email(
                user_email=user.email,
                subject="ACTIVATE YOUR ACCOUNT",
                uid64=uid,
                token=token,
            )
            return Response(
                {
                    "success": True,
                    "message": "Check your email for confirmation",
                }
            )
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

        if user is None:
            return Response({"success": False, "message": "Authentication Failed"})

        # Without activation, Login won't be allowed
        if user.is_active is False:
            return Response({"success": False, "message": "User is not activated"})

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


# Account Activation
@api_view(["GET"])
def activate(_, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except User.DoesNotExist:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return Response({"success": True, "message": "User is Verified"})
    else:
        return Response({"success": False, "message": "User is couldn't be verified"})


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


class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except AttributeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(
                serializer.validated_data.get("old_password", None)
            ):
                return Response(
                    {"success": False, "old_password": "Wrong password."}, status=400
                )
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response(
                {"success": True, "message": "Password updated successfully."}
            )
        return Response(serializer.errors, status=400)


class ResetPasswordView(APIView):
    def patch(self, request):
        s = ResetPasswordPayloadSerializer(data=request.data)
        if s.is_valid():
            uid64 = s.validated_data.get("uid64")
            token = s.validated_data.get("token")
            new_password = s.validated_data.get("new_password")
            try:
                uid = urlsafe_base64_decode(uid64).decode()
                user = User._default_manager.get(pk=uid)
            except User.DoesNotExist:
                user = None
                return Response({"success": False, "message": "Invalid Request 11"})
            isUserOK = user is not None
            isTokenOK = default_token_generator.check_token(user, token)

            # print("isUserOK", isUserOK)
            # print("isTokenOK", isTokenOK)

            if isUserOK is False:
                return Response(
                    {"success": False, "message": "User is couldn't be verified"}
                )

            if isTokenOK is False:
                return Response({"success": False, "message": "Invalid Request 22"})

            user.set_password(new_password)
            user.save()
            return Response(
                {"success": True, "message": "Password Reset was Successful"}
            )
        else:
            return Response({"success": False, "message": "Invalid Request 33"})

    # Requesting RESET LINK by POSTing the email
    def post(self, request):
        s = ResetPasswordSerializer(data=request.data)
        if s.is_valid():
            email = s.validated_data.get("email")
            user = None
            try:
                user = User.objects.get(email=email)
                token = default_token_generator.make_token(user)
                print("token ", token)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                print("uid ", uid)
                return Response(
                    {"success": True, "message": "Check Email to reset your password"}
                )
            except User.DoesNotExist:
                return Response({"success": False, "message": "User NOT found"})
        else:
            return Response({"success": False, "message": "Invalid Email"})
