# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-22 13:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsLearning', '0011_auto_20180722_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 7, 22, 13, 33, 21, 148109, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(error_messages={'blank': 'This field is not full', 'unique': 'This title is not unique'}, help_text='Must be a unique title', max_length=240, unique=True, verbose_name='Post title'),
        ),
    ]
