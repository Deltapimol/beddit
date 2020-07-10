from django.db import models
from django.contrib.auth.models import AbstractUser


class BlogUser(AbstractUser):

    email = models.EmailField(null=False, blank=False, max_length=30)
    password = models.CharField(null=False, blank=False, max_length=30)
    karma_points = models.IntegerField(null=True, default=0)
    is_mod = models.BooleanField(null=True)

    class Meta:
        managed = True
    
    def __str__(self):
        return self.first_name

    

    
