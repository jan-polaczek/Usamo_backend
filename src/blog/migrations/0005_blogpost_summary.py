# Generated by Django 2.2.10 on 2020-04-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200405_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]