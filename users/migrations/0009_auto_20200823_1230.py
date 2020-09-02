# Generated by Django 3.0.8 on 2020-08-23 08:00

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200822_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[100, 100], upload_to='avatars'),
        ),
    ]
