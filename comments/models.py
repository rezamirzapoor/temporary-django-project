from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import User
# Create your models here.

class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return super(CommentManager, self).filter(content_type=content_type, object_id=instance.id)
class Comment(models.Model):
    objects = CommentManager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    publish_date = jmodels.jDateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=50)
    content_object = GenericForeignKey('content_type', 'object_id')

    @property
    def published_at(self):
        return f"{str(self.publish_date.year)}/{str(self.publish_date.month)}/{str(self.publish_date.day)}"
    

    def is_parent(self):
        return True if not self.parent else False

    def replies(self):
        return Comment.objects.filter(parent=self)

    @property
    def reply_count(self):
        return self.replies().count()
    def __str__(self):
        return self.content
    def __unicode__(self):
        return str({
            "content": self.content,
            "user": self.user.email,
        })