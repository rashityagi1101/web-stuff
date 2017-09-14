# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0030_r_ad_details_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='user',
        ),
    ]
