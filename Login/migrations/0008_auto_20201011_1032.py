# Generated by Django 3.1 on 2020-10-11 08:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Login', '0007_auto_20201011_1031'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='following',
            unique_together={('follower', 'follow')},
        ),
    ]
