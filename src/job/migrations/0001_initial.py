# Generated by Django 2.2.10 on 2020-05-27 16:16

from django.db import migrations, models
import django.db.models.deletion
import job.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cv', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('offer_name', models.CharField(max_length=50)),
                ('offer_image', models.ImageField(null=True, upload_to=job.utils.create_job_offer_image_path)),
                ('salary_min', models.DecimalField(decimal_places=2, max_digits=8)),
                ('salary_max', models.DecimalField(decimal_places=2, max_digits=8)),
                ('company_name', models.CharField(max_length=70)),
                ('voivodeship', models.CharField(choices=[('dolnośląskie', 'dolnośląskie'), ('kujawsko-pomorskie', 'kujawsko-pomorskie'), ('lubelskie', 'lubelskie'), ('lubuskie', 'lubuskie'), ('łódzkie', 'łódzkie'), ('małopolskie', 'małopolskie'), ('mazowieckie', 'mazowieckie'), ('opolskie', 'opolskie'), ('podkarpackie', 'podkarpackie'), ('podlaskie', 'podlaskie'), ('pomorskie', 'pomorskie'), ('śląskie', 'śląskie'), ('świętokrzyskie', 'świętokrzyskie'), ('warmińsko-mazurskie', 'warmińsko-mazurskie'), ('wielkopolskie', 'wielkopolskie'), ('zachodniopomorskie', 'zachodniopomorskie')], max_length=30)),
                ('expiration_date', models.DateField()),
                ('description', models.CharField(max_length=1000)),
                ('removed', models.BooleanField(default=False, editable=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('zip_file', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobOfferCategory',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='JobOfferType',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='JobOfferApplication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('was_read', models.BooleanField(default=False)),
                ('document', models.FileField(null=True, upload_to='application_docs/')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_cv', to='cv.CV')),
                ('job_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.JobOffer')),
            ],
        ),
        migrations.AddField(
            model_name='joboffer',
            name='category',
            field=models.ForeignKey(db_column='category', null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.JobOfferCategory'),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='company_address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Address'),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='employer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.EmployerAccount'),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='offer_type',
            field=models.ForeignKey(db_column='offer_type', null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.JobOfferType'),
        ),
    ]
