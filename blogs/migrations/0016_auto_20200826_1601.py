# Generated by Django 3.0.8 on 2020-08-26 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_auto_20200826_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='publisher',
            new_name='owner',
        ),
    ]
