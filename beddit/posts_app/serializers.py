from rest_framework import serializers
from rest_framework import response
from .models import Discussion, Post, Comment, Reply


class DiscussionSerializer(serializers.ModelSerializer):    
     
    class Meta:
        model = Discussion
        fields = ['id', 'topic']
        
                   
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'discussion', 'post_title', 'post', 'created', 'points']
        

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'comment', 'commentator', 'created', 'points']
        

class ReplySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reply
        fields = ['id', 'comment', 'reply', 'respondent', 'created', 'points']
        
    