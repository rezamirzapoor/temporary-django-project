from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from users.models import User
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    UserListSerializer,
    UserDetailSerializer,
    UserCreateUpdateSerializer,
    GroupListSerializer,
    GroupCreateUpdateSerializer,
    PermissionSerializer
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import Group, Permission
# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        if self.action == 'rettieve':
            return UserDetailSerializer
        return UserCreateUpdateSerializer

    @action(methods=['get'], detail=False, url_path='profile', permission_classes=[IsAuthenticated])
    def profile(self, request):
        serializer = UserDetailSerializer(request.user.getUser())
        return Response(serializer.data)

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return GroupListSerializer
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return GroupCreateUpdateSerializer

class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
