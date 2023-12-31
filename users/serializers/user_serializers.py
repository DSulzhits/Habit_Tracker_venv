from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('avatar',)


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
