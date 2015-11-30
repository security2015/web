# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_pathname'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathname',
            name='pid',
            field=models.ForeignKey(default=datetime.datetime(2015, 11, 26, 4, 21, 38, 107030, tzinfo=utc), to='myapp.Document'),
            preserve_default=False,
        ),
    ]
