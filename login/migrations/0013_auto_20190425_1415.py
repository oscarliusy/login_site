# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-25 06:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20190425_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttemp',
            old_name='freight',
            new_name='freightFee',
        ),
    ]
