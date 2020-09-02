from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
from .models import Comment

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
            'object_id',
            'content_type',
            'parent',
        ]

class CommentListSerializer(ModelSerializer):
    user = SerializerMethodField()
    replies = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'user',
            'accepted',
            'content_type',
            'object_id',
            'published_at',
            'reply_count',
            'replies',
        ]
    def get_user(self, comment):
        return {
            'name': comment.user.name,
            'email': comment.user.email,
        }
    def get_replies(self, obj):
        if(obj.is_parent()):
            serializer = CommentListSerializer(obj.replies(), many=True)
            return serializer.data
        return None