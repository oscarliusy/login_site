# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-25 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_errorlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttemp',
            name='freight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, verbose_name='\u5b9e\u9645\u8fd0\u8d39(%)'),
        ),
        migrations.AddField(
            model_name='producttemp',
            name='tagpath',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='\u6807\u7b7e\u5730\u5740'),
        ),
    ]
