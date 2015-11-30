# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20151126_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=myapp.models.upload_to_unqiue_folder),
        ),
    ]
