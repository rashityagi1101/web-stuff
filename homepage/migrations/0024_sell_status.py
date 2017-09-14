# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0023_auto_20170505_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='status',
            field=models.CharField(default=b'not', max_length=250),
        ),
    ]
