from django.db import models
from django.utils import timezone
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Discussion(models.Model):

    topic = models.CharField(null=False, max_length=50)
    slug_topic = models.SlugField(max_length=80)

    class Meta:
        managed = True
        
        
    def __str__(self):
        return self.topic


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    post_title = models.CharField(null=False, blank=False, max_length=100)
    post = models.TextField(null=False, max_length=700)
    slug_post_title = models.SlugField(max_length=200)
    created = models.DateTimeField(auto_now=timezone.now(), null=True)
    points = models.IntegerField(default=0)

    class Meta:
        managed = True
    
    def __str__(self):
        return self.post_title


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(null=False, blank=False, max_length=300)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=timezone.now(), null=True)
    points = models.IntegerField(default=0)

    class Meta:
        managed = True
    
    def __str__(self):
        return self.comment


class Reply(models.Model):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField(null=False, blank=False, max_length=300)
    respondent = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=timezone.now(), null=True)
    points = models.IntegerField(default=0)

    class Meta:
        managed = True
    
    def __str__(self):
        return self.reply
