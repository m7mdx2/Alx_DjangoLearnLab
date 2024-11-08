from rest_framework import serializers
from rest_framework.authtoken.models import Token  
from django.contrib.auth import get_user_model
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Don't return password in responses
        }

    def create(self, validated_data):
        # Use get_user_model to ensure compatibility with custom user models
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            bio=validated_data.get('bio'),
            profile_picture=validated_data.get('profile_picture'),
        )
        # Set the password properly using set_password method
        user.set_password(validated_data['password'])
        user.save()
        serializers.CharField()
        
        # Create a token for the user upon successful registration
        Token.objects.create(user=user)
        return user
