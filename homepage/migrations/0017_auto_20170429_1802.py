# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_retailer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcomplain',
            name='status_update',
            field=models.CharField(default=b'', max_length=250),
        ),
    ]
