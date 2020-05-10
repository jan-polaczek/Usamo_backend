# Generated by Django 2.2.10 on 2020-05-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20200427_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.RunSQL('UPDATE job_joboffer SET confirmed = TRUE;')
    ]