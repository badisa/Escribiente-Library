# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150516_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.CharField(max_length=30),
        ),
    ]
