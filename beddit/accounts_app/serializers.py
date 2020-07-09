from rest_framework import serializers
from rest_framework import response
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'lasst_name', 'user_name', 'email', 'password', 'karma_points', 'is_mod']
        

   

