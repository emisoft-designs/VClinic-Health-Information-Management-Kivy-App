from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Patient

CustomUser = get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "password"]

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'password2', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate_username(self, username):
        if CustomUser.objects.filter(username=username).exists():
            detail = {
                "detail": "User Already exist!"
            }
            raise ValidationError(detail=detail)
        return username
    
    def validate(self, instance):
        if instance['password'] != instance['password2']:
            raise ValidationError({"message": "Both passwords must match!"})
        
        if CustomUser.objects.filter(email=instance['email']).exists():
            raise ValidationError({"message": "Email already taken!"})

        return instance

    def create(self, validated_data):
        password = validated_data.pop('password') 
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
