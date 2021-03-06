# Generated by Django 3.2.7 on 2021-10-06 21:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the car manufacturer/brand', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character')])),
                ('origin', models.CharField(help_text='Enter the country of origin', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Car model must be greater than 1 character')])),
                ('shape', models.CharField(help_text='Enter body shape', max_length=200)),
                ('mileage', models.PositiveBigIntegerField()),
                ('year', models.PositiveBigIntegerField()),
                ('area', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=300)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.make')),
            ],
        ),
    ]
