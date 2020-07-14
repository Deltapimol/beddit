from django.contrib import admin
from django.urls import path, include
from accounts_app import urls as account_urls
from posts_app import urls as posts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(account_urls)),
    path('',include(posts_urls)),
]
