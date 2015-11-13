# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0004_user_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=150, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
            preserve_default=True,
        ),
    ]
