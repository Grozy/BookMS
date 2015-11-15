# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0013_auto_20151115_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowhistory',
            name='is_over_time',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xb6\x8a\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userbaseinfo',
            name='avator_url',
            field=models.TextField(verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
            preserve_default=True,
        ),
    ]
