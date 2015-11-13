# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0005_auto_20151112_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_department',
            field=models.CharField(max_length=150, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=6, verbose_name=b'\xe5\xb7\xa5\xe5\x8f\xb7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_password',
            field=models.CharField(max_length=10, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81'),
            preserve_default=True,
        ),
    ]
