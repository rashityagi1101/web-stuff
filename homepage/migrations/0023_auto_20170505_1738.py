# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0022_rcomplain_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rcomplain',
            name='complain',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='rcomplain',
            name='status_update',
            field=models.CharField(default=b'unread', max_length=250),
        ),
    ]
