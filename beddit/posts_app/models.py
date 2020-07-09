from django.db import models
from django.utils import timezone
from accounts_app.models import User as blog_user


class Discussion(models.Model):

    topic = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.topic


class Post(models.Model):

    author = models.ForeignKey(blog_user, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, null=False, on_delete=models.CASCADE)
    post_title = models.CharField(null=False, blank=False, max_length=100)
    post = models.TextField(null=False, max_length=700)
    created = models.DateTimeField(auto_created=timezone.now(), null=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(null=False, blank=False, max_length=300)
    commentator = models.ForeignKey(blog_user, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=timezone.now(), null=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.comment


class Reply(models.Model):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField(null=False, blank=False, max_length=300)
    respondent = models.ForeignKey(blog_user, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=timezone.now(), null=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.reply
