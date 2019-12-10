# Generated by Django 2.2.7 on 2019-12-03 11:10

import cv.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='cv_pictures/')),
                ('date_of_birth', models.DateTimeField()),
                ('hobbies', models.CharField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CV')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year_start', models.PositiveIntegerField(default=2019, validators=[django.core.validators.MinValueValidator(1990), cv.models.max_value_current_year])),
                ('year_end', models.PositiveIntegerField(default=2019, validators=[django.core.validators.MinValueValidator(1990), cv.models.max_value_current_year])),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CV')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=20)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CV')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('year_start', models.PositiveIntegerField(default=2019, validators=[django.core.validators.MinValueValidator(1990), cv.models.max_value_current_year])),
                ('year_end', models.PositiveIntegerField(default=2019, validators=[django.core.validators.MinValueValidator(1990), cv.models.max_value_current_year])),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CV')),
            ],
        ),
    ]