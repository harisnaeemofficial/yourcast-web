# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-28 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0011_category_mask'),
    ]

    operations = [
        migrations.AddField(
            model_name='autostream',
            name='is_news',
            field=models.BooleanField(default=False),
        ),
    ]