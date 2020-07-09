from rest_framework import serializers
from rest_framework import response
from .models import Discussion, Post, Comment, Reply


class DiscussionSerializer(serializers.Serializer):
    
    class Meta:
        model = Discussion
        fields = ['id', 'topic']
        
        
class PostSerializer(serializers.Serializer):
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'discussion', 'post_title', 'post', 'created', 'points']


class CommentSerializer(serializers.Serializer):
    
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'commentator', 'created', 'points']


class ReplySerializer(serializers.Serializer):
    
    class Meta:
        model = Reply
        fields = ['id', 'reply', 'respondent', 'created', 'points']
    