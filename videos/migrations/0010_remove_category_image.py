# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-05 19:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_auto_20170205_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
