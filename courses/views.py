from django.shortcuts import render
from django.http import FileResponse
import os
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action

from .serializers import (
    CourseDetailSerializer,
    CourseListSerializer,
    CourseCreateUpdateSerializer,
    VideoListSerializer,
    VideoDetailSerializer,
    VideoCreateUpdateSerializer,
    PaymentListSerializer,
    PaymentCreateSerializer
)
from .models import Course, Video, Payment
from djangosite.permissions import IsOwnerOrReadOnly

# Create your views here.

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    # if user is teacher, you should get courses that owner is the teacher

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseCreateUpdateSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.getUser())
    
    @action(detail=True, url_path="comments", url_name="Get Comments")
    def comments(self, request, pk):
        comments = self.get_object().comments.all()
        json = [{
            "user": {
                "name": c.user.name,
                "avatar": c.user.avatar.url
            },
            "content": c.content,
            "parent": c.parent
        } for c in comments]
        return Response(json)


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return VideoListSerializer
        if self.action == 'retrieve':
            return VideoDetailSerializer
        return VideoCreateUpdateSerializer
    def perform_create(self, serializer):
        serializer.save(size=0, length=0)

    @action(detail=True, methods=['get'], permission_classes=[AllowAny], name="videos-download")
    def download(self, request, pk):
        video = self.get_object()
        return FileResponse(video.path.open(), 'r')
        # response['Content-Disposition'] = 'attachment; filename=file.mp4'
        

        

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    def get_queryset(self):
        user = None
        try:
            user = self.request.user.getUser()
        except:
            user = None
        if user:
            return Payment.objects.filter(user=user)
    def get_serializer_class(self):
        return PaymentListSerializer if self.action == 'list' else PaymentCreateSerializer