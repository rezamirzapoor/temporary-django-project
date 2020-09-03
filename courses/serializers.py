from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
from .models import Course, Video, Payment
class VideoListSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        
class CourseDetailSerializer(ModelSerializer):
    owner = SerializerMethodField()
    videos = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'owner',
            'videos',
            'published_at',
            'thumbnail',
            'description',
            'price',
            'off',
            'categories',
            'episodes_count',
            'content_type',
        ]
        depth = 1
    def get_owner(self, course):
        return {
            'name': course.owner.name,
            'avatar': self.context.get('request').build_absolute_uri(course.owner.avatar.url),
        }
    def get_videos(self, course):
        return VideoListSerializer(course.video_set.all(), many = True).data

class CourseListSerializer(ModelSerializer):
    
    owner = SerializerMethodField()
    thumbnail = SerializerMethodField()
    comments_count = SerializerMethodField()
    categories = SerializerMethodField()
    # url = serializers.HyperlinkedIdentityField(view_name='courses:detail') # we can add loockup_field
    detail_url = HyperlinkedIdentityField(view_name='course-detail') # we can add loockup_field
    class Meta:
        model = Course
        # fields = '__all__'
        fields = [
            'id',
            'title',
            'owner',
            'published_at',
            'thumbnail',
            'description',
            'price',
            'off',
            'episodes_count',
            'comments_count',
            'categories',
            'detail_url',
        ]

    def get_owner(self, obj):
        # return str(obj.owner.name)
        return {
            "name": obj.owner.name,
            "email": obj.owner.email,
        }
    def get_thumbnail(self, obj):
        return self.context['request'].build_absolute_uri(obj.thumbnail.url) if obj.thumbnail else 'http://localhost:8000/media/images/1.jpeg'
    def get_comments_count(self, obj):
        return obj.comments.count()
    def get_categories(self, obj):
        return [c.title for c in obj.categories.all()]
    

class CourseCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'title',
            'price',
            'thumbnail',
            'off',
            'description',
            'categories'
        ]


class VideoDetailSerializer(ModelSerializer):
    path = SerializerMethodField()
    download_link = HyperlinkedIdentityField(view_name="videos-download")
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'episode',
            'path',
            'size',
            'length',
            'is_lock',
            'course',
            'download_link'
        ]
    def get_path(self, obj):
        return self.context['request'].build_absolute_uri(obj.path) if not obj.is_lock else ""

class VideoCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'path',
            'episode',
            'course',
            'is_lock'
        ]

class PaymentListSerializer(ModelSerializer):
    user = SerializerMethodField()
    course = SerializerMethodField()
    class Meta:
        model = Payment
        fields = [
            'id',
            'user',
            'course',
            'resnumber',
            'jalali_date',
            'expense'
        ]
    def get_user(self, payment):
        return {
            "name": payment.user.name,
        }
    def get_course(self, payment):
        return {
            "title": payment.course.title
        }
class PaymentCreateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
