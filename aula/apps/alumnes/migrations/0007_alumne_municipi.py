# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnes', '0006_auto_20180507_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumne',
            name='municipi',
            field=models.CharField(blank=True, max_length=240),
        ),
    ]
