# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-29 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0019_auto_20161129_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]