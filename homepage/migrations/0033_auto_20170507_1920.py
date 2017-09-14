# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0032_sell_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='retailer_details',
            field=models.ForeignKey(blank=True, to='homepage.retailer', null=True),
        ),
    ]
