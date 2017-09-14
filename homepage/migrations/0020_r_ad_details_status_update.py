# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_auto_20170430_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='r_ad_details',
            name='status_update',
            field=models.BooleanField(default=False),
        ),
    ]
