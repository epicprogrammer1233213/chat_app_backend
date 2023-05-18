from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')  # Refer to user of the profile

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')  # Refer to user of the profile

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user.username')  # Refer to user of the profile

    class Meta:
        model = Like
        fields = ['id', 'post', 'user']
