# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0024_sell_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='status',
            field=models.ForeignKey(to='homepage.r_ad_details'),
        ),
    ]
