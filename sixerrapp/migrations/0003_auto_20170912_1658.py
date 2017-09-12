# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-09-12 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixerrapp', '0002_gig'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gig',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='gig',
            name='price',
        ),
        migrations.RemoveField(
            model_name='gig',
            name='status',
        ),
        migrations.RemoveField(
            model_name='gig',
            name='user',
        ),
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('GD', 'Graphics & Design'), ('DM', 'Digital & Marketing'), ('VA', 'Video & Animation'), ('MA', 'Music & Audio'), ('PT', 'Programming & Tech')], max_length=2),
        ),
    ]
