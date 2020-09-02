from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Comment
from .serializers import CommentListSerializer, CommentCreateSerializer


# Create your views here.

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.filter(parent=None)
    def get_serializer_class(self):
        return CommentListSerializer if self.action == 'list' else CommentCreateSerializer 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user.getUser())
