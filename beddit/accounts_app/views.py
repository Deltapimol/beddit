from django.shortcuts import render
from rest_framework import viewsets
from .models import BlogUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = BlogUser.objects.all()
