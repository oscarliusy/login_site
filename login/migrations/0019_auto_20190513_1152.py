# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-13 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_auto_20190513_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymaterial',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='\u91c7\u8d2d\u4ef7(rmb)'),
        ),
        migrations.AlterField(
            model_name='outitem',
            name='freightfee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u8fd0\u8d39'),
        ),
        migrations.AlterField(
            model_name='outitem',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, verbose_name='\u5305\u88c5\u4f53\u79ef(m3)'),
        ),
        migrations.AlterField(
            model_name='outitem',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, verbose_name='\u5305\u88c5\u91cd\u91cf(kg)'),
        ),
        migrations.AlterField(
            model_name='outstock',
            name='total_freightfee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u603b\u8fd0\u8d39(rmb)'),
        ),
        migrations.AlterField(
            model_name='outstock',
            name='total_volume',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='\u603b\u4f53\u79ef(m3)'),
        ),
        migrations.AlterField(
            model_name='outstock',
            name='total_weight',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='\u603b\u91cd\u91cf(kg)'),
        ),
        migrations.AlterField(
            model_name='preoutstock',
            name='total_freightfee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u603b\u8fd0\u8d39(rmb)'),
        ),
        migrations.AlterField(
            model_name='preoutstock',
            name='total_volume',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='\u603b\u4f53\u79ef(m3)'),
        ),
        migrations.AlterField(
            model_name='preoutstock',
            name='total_weight',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='\u603b\u91cd\u91cf(kg)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='adcost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u5e7f\u544a\u8d39(dollar)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='amazonReferralFee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='amazon\u5e73\u53f0\u8d39(%)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='amazonSalePrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u552e\u4ef7(dollar)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='currency',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=15, null=True, verbose_name='\u6c47\u7387(us-chn)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='dhlShippingFee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='DHL\u6d77\u8fd0\u8d39(rmb)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='fbaFullfillmentFee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='FBA\u8fd0\u8d39(dollar)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='freightFee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u5b9e\u9645\u8fd0\u8d39(%)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u5305\u88c5\u5c3a\u5bf8\u9ad8(cm)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u5305\u88c5\u5c3a\u5bf8\u957f(cm)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='margin',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='\u5229\u6da6(dollar)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='marginRate',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='\u5229\u6da6\u7387(%)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='opFee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u8fd0\u8425\u8d39(rmb)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='packageFee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u7269\u6599\u8d39(rmb)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='payoneerServiceFee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Payoneer\u670d\u52a1\u8d39(%)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='purchasePrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u91c7\u8d2d\u4ef7\u683c(rmb)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='shrinkage',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u4ea7\u54c1\u635f\u8017(dollar)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='volumeWeight',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='\u5305\u88c5\u4f53\u79ef\u91cd(kg)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='\u5305\u88c5\u91cd\u91cf(kg)'),
        ),
        migrations.AlterField(
            model_name='producttemp',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='\u5305\u88c5\u5c3a\u5bf8\u5bbd(cm)'),
        ),
    ]