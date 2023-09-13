from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from API.models import User
from API.choices import UserTypeChoices


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="El email ingresdo ya se encuentra en uso.",
            ),
        ],
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "user_type"]
        extra_kwargs = {
            "password": {"write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def save(self, **kwargs):
        user = User(
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            username=self.validated_data["email"],
            email=self.validated_data["email"],
            user_type=self.validated_data.get("user_type", UserTypeChoices.USER),
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()

        return user


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
        except Exception as exc:
            raise Exception("No se encuentra una cuenta activa") from exc

        data.update({"id": self.user.id})
        data.update({"user_type": self.user.user_type})
        return data
