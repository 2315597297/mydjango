# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-03 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171003_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=3900000000),
        ),
    ]
