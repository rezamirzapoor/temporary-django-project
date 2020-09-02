# Generated by Django 3.0.8 on 2020-08-20 17:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_user_favorite_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('thumbnail', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[1920, 1080], upload_to='images')),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=128)),
                ('off', models.IntegerField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('episode', models.IntegerField()),
                ('path', models.FileField(upload_to='videos')),
                ('size', models.IntegerField()),
                ('length', models.IntegerField()),
                ('is_look', models.BooleanField(default=False)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
    ]
