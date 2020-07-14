from rest_framework import serializers
from rest_framework import response
from .models import BlogUser


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogUser
        fields = '__all__'
        

   

