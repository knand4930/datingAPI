from django.contrib.auth.password_validation import validate_password
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from account.models import Passion, UserMedia, BodyType, Education, MaritalStatus, Gender, IdealMatch

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('password', 'email', 'first_name', 'last_name')


class UserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = "__all__"
        exclude = ["email", "password"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('password', 'email', 'first_name', 'last_name',)
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'is_root_user': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ['password', 'user_permissions', 'groups', 'is_staff', 'root_uuid', 'is_root_user', 'is_team_member',
                   'is_superuser', 'is_admin']


class RegisterPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "phone", "email", "first_name", "last_name"]
        extra_kwargs = {
            "id": {"read_only": True},
            "phone": {"required": True},
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class PassionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passion
        fields = ["id", 'passion', 'image', 'color']


class IdealMatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = IdealMatch
        fields = ["id", 'ideal_match', 'image', 'color']


class GenderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ["id", 'gender', 'image', 'color']


class MaritalStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ["id", 'marital_status', 'image', 'color']


class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ["id", 'education', 'image', 'color']


class BodyTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ["id", 'body', 'image', 'color']


class UserMediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserMedia
        fields = ["id", 'video', 'image']


class UserMediaPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserMedia
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['user'].user
        value = UserMedia(**validated_data)
        value.user = user
        value.save()

        return value
