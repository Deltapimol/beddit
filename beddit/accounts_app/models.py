from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    first_name = models.CharField(null=False, max_length=30)
    last_name = models.CharField(null=False, max_length=30)
    user_name = models.CharField(null=False, max_length=30)
    email = models.EmailField(null=False, max_length=50)
    password = models.CharField(null=False, max_length=40)
    karma_points = models.IntegerField(default=0)
    is_mod = models.BooleanField(null=True)

    def __str__(self):
        return self.first_name
