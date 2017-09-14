# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0025_auto_20170506_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r_ad_details',
            name='status_update',
            field=models.CharField(max_length=250),
        ),
    ]
