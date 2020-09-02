from django.db import models
from django.contrib.contenttypes.models import ContentType
from django_resized import ResizedImageField
from users.models import User
from django.utils import timezone
from django_jalali.db import models as jmodels
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from categories.models import Category
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=128)
    thumbnail = ResizedImageField(upload_to = 'images', null=True, blank = True)
    description =  models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, models.CASCADE)
    price = models.CharField(max_length=128, default='0')
    off = models.IntegerField(default=0)
    published_datetime = jmodels.jDateTimeField(default=timezone.now, blank=True)
    comments = GenericRelation(Comment)
    categories = models.ManyToManyField(Category, blank=True)
    
    @property
    def new_price(self):
        return int(self.price) * (100 - self.off)
    @property
    def published_at(self):
        return f"{str(self.published_datetime.year)}/{str(self.published_datetime.month)}/{str(self.published_datetime.day)}"
    @property
    def episodes_count(self):
        return self.video_set.all().count()
    @property
    def content_type(self):
        # return str(ContentType.objects.get_for_model(self.__class__))
        return ContentType.objects.get_for_model(self.__class__).id
    def __str__(self):
        return self.title
        
class Video(models.Model):
    title = models.CharField(max_length=128)
    episode = models.IntegerField()
    path = models.FileField(upload_to='videos')
    size = models.IntegerField(blank = True)
    length = models.IntegerField(blank = True)
    is_lock = models.BooleanField(default=False, blank = True)
    upload_date = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    published_datetime = jmodels.jDateTimeField(default=timezone.now, blank=True)

    @property
    def published_at(self):
        return f"{str(self.published_datetime.year)}/{str(self.published_datetime.month)}/{str(self.published_datetime.day)}"
    def __str__(self):
        return self.title

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resnumber = models.CharField(max_length=20)
    expense = models.CharField(max_length=20, default='0')
    timestamp = jmodels.jDateTimeField(auto_now_add=True)
    @property
    def jalali_date(self):
        return f"{str(self.timestamp.year)}/{str(self.timestamp.month)}/{str(self.timestamp.day)}"

    def __str__(self):
        return self.resnumber