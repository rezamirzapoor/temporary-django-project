from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
from .models import Blog, Category
from comments.models import Comment

class BlogDetailSerializer(ModelSerializer):
    owner = SerializerMethodField() 
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'content',
            'thumbnail',
            'published_at',
            'time_for_read',
            'categories',
            'owner',
            # 'comments',
            'comments_count',
            'likes_count',
            'content_type',
        ]
        depth = 1
    def get_owner(self, obj):
        return {
            'name': obj.owner.name,
            'avatar': self.context.get('request').build_absolute_uri(obj.owner.avatar.url),
        }
    # def get_comments(self, obj):
    #     query = Comment.objects.filter_by_instance(obj).filter(accepted=True)
    #     return [{
    #         "user": {
    #             "name": c.user.name,
    #             "avatar": self.context["request"].build_absolute_uri(c.user.avatar.url)
    #         },
    #         "content": c.content,
    #         "parent": c.parent
    #     } for c in query]
    # def get_categories(self, blog):
    #     return [c.title for c in blog.categories.all()]

class BlogListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(view_name='blogs-detail')
    owner = SerializerMethodField()
    categories = SerializerMethodField()
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'content',
            'thumbnail',
            'published_at',
            'time_for_read',
            'categories',
            'owner',
            'comments_count',
            'likes_count',
            'content_type',
            'detail_url'
        ]
        depth = 1
    def get_owner(self, obj):
        return {
            'name': obj.owner.name,
            'avatar': self.context.get('request').build_absolute_uri(obj.owner.avatar.url),
        }
    def get_categories(self, blog):
        return [c.title for c in blog.categories.all()]

class BlogCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'title',
            'content',
            'thumbnail',
            'categories',
        ]
    