from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

from django.utils import timezone
from django_jalali.db import models as jmodels
from django_resized import ResizedImageField

from categories.models import Category
from users.models import User
from comments.models import Comment
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=128, unique=True, null=False)
    content = models.TextField(null=True, blank=True)
    thumbnail = ResizedImageField(upload_to='images', size=[300, 300], quality = 100, null=True, blank=True)
    publish_date = jmodels.jDateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    comments = GenericRelation(Comment)

    @property
    def published_at(self):
        return f"{str(self.publish_date.year)}/{str(self.publish_date.month)}/{str(self.publish_date.day)}"
    @property
    def time_for_read(self):
        return (len(self.content) * 0.001).__round__()
    @property
    def brief_content(self):
        if len(self.content) > 100:
            return self.content[:100] + ' ...'
        return self.content
    @property
    def comments_count(self):
        return self.comments.all().count()
    @property
    def likes_count(self):
        return self.user_set.all().count()
    @property
    def content_type(self):
        return ContentType.objects.get_for_model(self.__class__).id

    def related_blogs(self):
        return Blog.objects.filter(categories__in = self.categories.all())[:5]
        
    def __str__(self):
        return self.title
    def __unicode__(self):
        return str({
            'title': self.title,
            'content': self.content,
            'thumbnail': self.thumbnail.url,
            'publish_date': self.publish_date,
            'publisher': self.publisher,
            'categories': self.categories.all()
        })