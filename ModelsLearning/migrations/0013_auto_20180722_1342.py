# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-22 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsLearning', '0012_auto_20180722_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='publish_data',
            new_name='publish_date',
        ),
    ]
