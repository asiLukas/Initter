# Generated by Django 3.1 on 2020-08-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20200826_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date', 'created']},
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.TimeField(default='11:17:54'),
        ),
    ]