# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_crop_cimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='rcomplain',
            name='complain',
            field=models.CharField(default=b'', max_length=250),
        ),
        migrations.AddField(
            model_name='rcomplain',
            name='status_update',
            field=models.CharField(default=b'', max_length=250),
        ),
    ]
