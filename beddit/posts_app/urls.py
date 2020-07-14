from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DiscussionViewSet, PostsViewSet, CommentViewSet, ReplyViewSet


router = DefaultRouter()
router.register(r'discussion', DiscussionViewSet, basename='discussion')
router.register(r'posts', PostsViewSet, basename='posts')
router.register(r'comment', CommentViewSet, basename='commment')
router.register(r'reply', ReplyViewSet, basename='reply')

urlpatterns = router.urls