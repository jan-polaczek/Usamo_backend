# Generated by Django 2.2.8 on 2020-02-12 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20191209_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('company_name', models.CharField(max_length=60)),
                ('company_address', models.CharField(max_length=120)),
                ('status', models.IntegerField(choices=[(1, 'Verified'), (2, 'Waiting for verification'), (3, 'Not verified')], default=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
