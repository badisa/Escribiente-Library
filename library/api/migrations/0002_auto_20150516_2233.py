# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='descript',
            field=models.TextField(default=b'No Description'),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=b'', max_length=13),
        ),
        migrations.AddField(
            model_name='book',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='copies',
            field=models.CharField(max_length=30),
        ),
    ]
