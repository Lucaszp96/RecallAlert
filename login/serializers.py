from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


# Override some methods of the TokenObtainPairSerializer class to implement a custom data response structure
# and payload content
class MyTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super.get_token(user)
        token['name'] = user.username

        return token

    def validate(self, attrs):
        # data is a dictionary
        # Its structure is: {'refresh': 'token used to refresh token', 'access': 'Token value used to authenticate'}
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['token'] = data['access']

        del data['access']

        data['expire'] = refresh.access_token.payload['exp']  # 有效期

        data['username'] = self.user.username

        data['email'] = self.user.email

        return data


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    code = serializers.CharField(write_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'id',
            'nickname',
            'username',
            'password',
            'confirm_password',
            'sex',
            'code'
        ]

    default_error_messages = {
        'code_error': 'Error',
        'password_error': 'Password not match',
        "username_error": 'Username Error',
    }

