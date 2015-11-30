# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20151126_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='path',
            field=models.CharField(default=datetime.datetime(2015, 11, 26, 2, 40, 17, 534856, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
