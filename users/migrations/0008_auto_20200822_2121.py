# Generated by Django 3.0.8 on 2020-08-22 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200822_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='verified',
        ),
    ]
