# Generated by Django 2.2.10 on 2020-05-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0002_userperspective'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userperspective',
            name='substep_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
