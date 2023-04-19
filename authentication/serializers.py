from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model()(
            username=validated_data['username'],
            email=validated_data['email'],
            is_superuser=validated_data.get('is_superuser', False),
            is_staff=validated_data.get('is_staff', False),
            is_active=validated_data.get('is_active', True),
            bio=validated_data.get('bio', None),
            profile_picture=validated_data.get('profile_picture', None),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

