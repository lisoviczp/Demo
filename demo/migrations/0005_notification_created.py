# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20160123_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 24, 20, 15, 15, 208832, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
