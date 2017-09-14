# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20170415_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='cimage',
            field=models.ImageField(default=b'Desktop/None/no-img.jpg', upload_to=b'Desktop/'),
        ),
    ]
