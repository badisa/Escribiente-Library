# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=80, blank=True)),
                ('published', models.PositiveIntegerField(default=1900)),
                ('copies', models.PositiveIntegerField(default=0)),
                ('checked_out', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
