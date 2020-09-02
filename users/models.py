from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_resized import ResizedImageField

from .managers import CustomUserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=128, null=False)
    name = models.CharField(max_length=128)
    avatar = ResizedImageField(size=[100, 100], upload_to = 'avatars', quality = 100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    favorite_blogs = models.ManyToManyField('blogs.Blog', blank=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.email
    def __unicode__(self):
        return str({
            'id': self.pk,
            'name': self.name,
            'email':self.email,
            'password': self.password,
            'avatar': self.avatar.url,
            })
    # class Meta:
    #     db_table = 'users'