# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='page_num',
            field=models.IntegerField(default=0),
        ),
    ]
