from django.contrib import admin
from .models import Discussion, Post, Comment, Reply


admin.site.register(Discussion)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
