# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0026_auto_20170506_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='status',
        ),
    ]
