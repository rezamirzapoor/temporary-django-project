from django.contrib import admin
from .models import User

admin.site.register(model_or_iterable = [User])
# Register your models here.
