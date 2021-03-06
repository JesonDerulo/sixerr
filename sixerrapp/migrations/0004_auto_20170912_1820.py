# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-09-12 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sixerrapp', '0003_auto_20170912_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='gig',
            name='photo',
            field=models.FileField(blank=True, upload_to='gigs'),
        ),
        migrations.AddField(
            model_name='gig',
            name='price',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='gig',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
