from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework import routers


from blogs.views import BlogViewSet
from courses.views import CourseViewSet, PaymentViewSet, VideoViewSet
from categories.views import CategoryViewSet
from comments.views import CommentViewSet
from users.views import GroupViewSet, PermissionViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet, 'blogs')
router.register(r'courses', CourseViewSet)
router.register(r'videos', VideoViewSet, 'videos')
router.register(r'categories', CategoryViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]