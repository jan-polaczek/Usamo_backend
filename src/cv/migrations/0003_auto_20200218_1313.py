# Generated by Django 2.2.8 on 2020-02-18 12:13

import cv.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20200218_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='cv',
        ),
        migrations.AddField(
            model_name='feedback',
            name='cv_id',
            field=models.IntegerField(default=1, validators=[cv.models.validate_cv_id]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
