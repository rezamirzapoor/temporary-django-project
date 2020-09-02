from django.contrib import admin
from .models import Course, Video, Payment
# Register your models here.

admin.site.register([Course, Video, Payment])