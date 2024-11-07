from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User

# from rest_framework import viewsets

from people.serializers import RegistrationSerializer, UserListSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode  # , urlsafe_base64_decode
from django.utils.encoding import force_bytes

# from django.contrib.auth.models import User

# from django.contrib.auth import authenticate, login, logout
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
