# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-20 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsLearning', '0005_postmodel_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='postmodel',
            name='publish',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('private', 'Private')], default='draft', max_length=120),
        ),
    ]
