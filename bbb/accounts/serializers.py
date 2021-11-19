from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings


User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"],
                                   checkpw=validated_data["checkpw"],
                                   name=validated_data["name"],
                                   phone_number=validated_data["phone_number"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["pk", "username", "password", "checkpw", "name", "phone_number"]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'id', "name"]

class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['token', 'username', 'name', 'password']





