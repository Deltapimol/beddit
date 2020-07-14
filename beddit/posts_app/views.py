from django.shortcuts import render
from rest_framework import viewsets
from .models import Discussion, Post, Comment, Reply
from .serializers import DiscussionSerializer, PostSerializer, CommentSerializer, ReplySerializer


class DiscussionViewSet(viewsets.ModelViewSet):
    serializer_class = DiscussionSerializer
    queryset = Discussion.objects.all()


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class ReplyViewSet(viewsets.ModelViewSet):
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()




    


