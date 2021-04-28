from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import ConfirmationCode, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    role = serializers.CharField(max_length=10)
    bio = serializers.CharField(max_length=500)

    class Meta:
        fields = ['username', 'email', 'role', 'bio']
        model = CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = CustomUser.email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False   

    def validate(self, attrs):
        attrs['password'] = self.context['request'].data.get('confirmation_code')
        return super().validate(attrs)


class ConfirmationCodeSerializer(serializers.Serializer):
    confirmation_code = serializers.SlugRelatedField(
        slug_field='confirmation_code',
        many=False,
        read_only=True
    )
    email = serializers.SlugRelatedField(
        slug_field='email',
        many=False,
        read_only=True
    )
    code_date = serializers.DateTimeField()    

    class Meta:
        fields = '__all__'
        model = ConfirmationCode
