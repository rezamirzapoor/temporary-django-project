from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import FileResponse
from blogs.models import Blog, Category, Comment
from users.models import User
from comments.serializers import CommentListSerializer
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins, generics
from rest_framework.decorators import action
from .serializers import (
    BlogDetailSerializer,
    BlogListSerializer,
    BlogCreateUpdateSerializer,
)
from rest_framework_simplejwt import authentication
# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        query = Blog.objects
        category = self.request.GET.get('category')
        search = self.request.GET.get('search')
        if self.action == 'list':
            if category:
                query = query.filter(categories=category)
            if search:
                query = query.filter(title__contains = search)
        return query.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogListSerializer
        if self.action == 'retrieve':
            return BlogDetailSerializer
        return BlogCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.getUser())

    @action(detail=True, permission_classes=[permissions.IsAuthenticated], url_path='like-or-unlike')
    def like_or_unlike(self, request, pk):
        favorite_blogs = request.user.getUser().favorite_blogs
        print(int(pk) in [f.id for f in favorite_blogs.all()])
        favorite_blogs.remove(self.get_object()) if int(pk) in [f.id for f in favorite_blogs.all()] else favorite_blogs.add(self.get_object())
        return Response({"message": "changed status"})

    @action(detail=True, url_path="comments", url_name="Get Comments")
    def comments(self, request, pk):
        comments = self.get_object().comments.filter(parent=None)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)