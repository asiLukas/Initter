# Generated by Django 3.1 on 2020-08-27 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0015_auto_20200827_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='auth.User', max_length=120),
        ),
    ]
