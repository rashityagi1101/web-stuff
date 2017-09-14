# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0034_auto_20170507_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r_ad_details',
            name='status_update',
            field=models.CharField(default=b'unread', max_length=250),
        ),
    ]
