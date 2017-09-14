# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0033_auto_20170507_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='retailer_details',
            field=models.ForeignKey(related_name='retailer_details', default=2, to=settings.AUTH_USER_MODEL),
        ),
    ]
