from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
from .models import Category
from blogs.serializers import BlogListSerializer

class CategoryListSerializer(ModelSerializer):
    blogs_count = SerializerMethodField()
    detail_url = HyperlinkedIdentityField(view_name='category-detail')
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'blogs_count',
            'detail_url'
        ]
    def get_blogs_count(self, category):
        return category.blog_set.count()

class CategoryDetailSerializer(ModelSerializer):
    blogs = SerializerMethodField()
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'blogs',
        ]
    
    def get_blogs(self, category):
        # return BlogListSerializer(category.blog_set.all(), many = True).data
        return [{
        "id": b.pk,
        "title": b.title,
        "content": b.content,
        "thumbnail": self.context['request'].build_absolute_uri(b.thumbnail.url),
        "published_at": b.published_at,
        "time_for_read": b.time_for_read,
        "owner": {
            "name": b.owner.name,
            "avatar": self.context['request'].build_absolute_uri(b.owner.avatar.url)
        },
        "comments_count": b.comments_count,
        "likes_count": b.likes_count
        } for b in category.blog_set.all()]