import base64
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers

from people.models import People
from transaction.constants import DEPOSIT
from transaction.models import Transaction


# Custom Validators
def validate_base64(value):
    try:
        # Decode the base64 encoded string
        decoded_value = urlsafe_base64_decode(value)
        # Check if the decoded value is a valid integer (user primary key)
        int(decoded_value)
        return value
    except (ValueError, TypeError, base64.binascii.Error):
        raise serializers.ValidationError("Invalid base64 encoded user ID")


# ============= End of Custom Validators ===========================


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ["image_url", "phone_no"]


class UserListSerializer(serializers.ModelSerializer):
    people_info = PeopleSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "people_info",
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    # confirm_password = serializers.CharField(required=True)
    image_url = serializers.URLField(required=True)
    phone_no = serializers.CharField(max_length=12)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            # "confirm_password",
            "image_url",
            "phone_no",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        isEmailExist = User.objects.filter(email=validated_data["email"]).exists()
        isUsernameExist = User.objects.filter(
            username=validated_data["username"]
        ).exists()
        if isEmailExist:
            raise serializers.ValidationError({"error": "Email Already exists"})
        if isUsernameExist:
            raise serializers.ValidationError({"error": "Username Already exists"})
        image_url = validated_data.pop("image_url")
        phone_no = validated_data.pop("phone_no")

        # Extract password and hash it
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.is_active = False
        user.save()

        # Create the People instance
        current_people = People.objects.create(
            basic_info=user,
            image_url=image_url,
            phone_no=phone_no,
            active_status=False,
            balance=0.00,
        )
        user.people_info = current_people

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=2028, required=True)
    password = serializers.CharField(max_length=2028, required=True)


class BalanceDepositeSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(decimal_places=2, default=0.00, max_digits=12)
    transaction_id = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = People
        fields = ["balance", "amount", "transaction_id"]

    def update(self, instance, validated_data):
        instance.balance += validated_data["amount"]
        instance.save()
        single_transaction = Transaction(
            type=DEPOSIT,
            amount=validated_data["amount"],
            transaction_id=validated_data["transaction_id"],
            buyer=self.context["request"].user,
        )
        single_transaction.save()
        return instance


class BalanceCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ["balance"]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, max_length=2028)
    new_password = serializers.CharField(required=True, max_length=2028)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=2028)


class ResetPasswordPayloadSerializer(serializers.Serializer):
    uid64 = serializers.CharField(validators=[validate_base64])
    token = serializers.CharField(required=True, max_length=1024)
    new_password = serializers.CharField(required=True, max_length=150)
