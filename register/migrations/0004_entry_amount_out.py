# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20170126_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='amount_out',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
