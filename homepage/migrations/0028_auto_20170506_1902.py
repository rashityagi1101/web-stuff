# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0027_remove_sell_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r_ad_details',
            name='crop_details',
            field=models.ForeignKey(blank=True, to='homepage.crop', null=True),
        ),
        migrations.AlterField(
            model_name='r_ad_details',
            name='qty_details',
            field=models.ForeignKey(blank=True, to='homepage.qty', null=True),
        ),
        migrations.AlterField(
            model_name='r_ad_details',
            name='retailer_details',
            field=models.ForeignKey(blank=True, to='homepage.retailer', null=True),
        ),
    ]
