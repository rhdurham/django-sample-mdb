# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20151008_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviereview',
            name='url',
        ),
    ]
