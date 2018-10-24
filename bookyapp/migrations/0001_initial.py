# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 11:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('location', models.CharField(choices=[('nakuru', 'nakuru'), ('nyeri', 'nyeri'), ('mombasa', 'mombasa')], max_length=80, null=True)),
                ('date_booked', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('vehicLe_number', models.CharField(choices=[('high', 'high'), ('average', 'average'), ('low', 'low')], max_length=80, null=True)),
                ('location', models.CharField(max_length=80)),
            ],
        ),
    ]
