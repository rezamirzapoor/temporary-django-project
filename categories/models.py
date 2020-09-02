from django.db import models
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return {
            "title": self.title
        }