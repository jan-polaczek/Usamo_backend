# Generated by Django 2.2.10 on 2020-04-07 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200406_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostheader',
            name='blog_post',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost'),
        ),
    ]