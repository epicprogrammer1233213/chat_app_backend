from rest_framework import serializers
from .models import Connection

class ConnectionSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.user.username')
    following = serializers.ReadOnlyField(source='following.user.username')

    class Meta:
        model = Connection
        fields = ['id', 'follower', 'following', 'created_at']
