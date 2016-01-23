# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demo', '0003_auto_20160123_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='sending_user',
            field=models.ForeignKey(related_name='sending_user', default=2, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(related_name='receiving_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
