import email
from pyexpat import model
from unicodedata import name

#from attr import fields
#from questionary import password
from rest_framework import serializers
from profiles_api import models


class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our views"""
    name = serializers.CharField(max_length=10)


# create userprofile serializer to overwrite existing models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': 'True',
                'style': {'input_style': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return A new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account password"""
        if 'password' is validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
