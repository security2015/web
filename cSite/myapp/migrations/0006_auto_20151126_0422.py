# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_pathname_pid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pathname',
            old_name='path',
            new_name='npath',
        ),
    ]
