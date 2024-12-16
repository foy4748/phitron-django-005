from django.contrib.auth.models import User
from rest_framework import serializers

from people.models import People


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

    class Meta:
        model = People
        fields = ["balance", "amount"]

    def update(self, instance, validated_data):
        instance.balance += validated_data["amount"]
        instance.save()
        return instance


class BalanceCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ["balance"]
