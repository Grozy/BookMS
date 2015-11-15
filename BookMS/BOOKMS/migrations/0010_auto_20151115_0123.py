# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0009_auto_20151115_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_logo_url',
            field=models.CharField(default=b'', max_length=150, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(default=b'', max_length=150, verbose_name='\u4e66\u540d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userbaseinfo',
            name='account',
            field=models.CharField(default=b'', max_length=30, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userbaseinfo',
            name='avator_url',
            field=models.CharField(default=b'', max_length=150, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userbaseinfo',
            name='name',
            field=models.CharField(default=b'', max_length=16, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userbaseinfo',
            name='password',
            field=models.CharField(default=b'', max_length=16, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81'),
            preserve_default=True,
        ),
    ]
