# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150516_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='checked_out',
            field=models.IntegerField(default=0),
        ),
    ]
