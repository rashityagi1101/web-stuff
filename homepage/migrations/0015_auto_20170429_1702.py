# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_auto_20170420_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcomplain',
            name='status_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rcomplain',
            name='status_update',
            field=models.BooleanField(default=False),
        ),
    ]
