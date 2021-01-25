# Generated by Django 3.1.3 on 2020-11-26 03:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('w_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('ward_id', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('d_stage', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('doctor_id', models.ManyToManyField(to='doctor.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(default='Male', max_length=100)),
                ('street_address', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('zip_code', models.CharField(default='43701', max_length=6)),
                ('p_level', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('w_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.ward')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('patient_id', models.ManyToManyField(to='patients.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('first_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('patient_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
            options={
                'unique_together': {('patient_id', 'first_name')},
            },
        ),
    ]