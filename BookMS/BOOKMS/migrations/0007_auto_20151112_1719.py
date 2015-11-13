# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0006_auto_20151112_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='body',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.CharField(max_length=150, verbose_name=b'\xe4\xb9\xa6\xe5\x90\x8d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='createTime',
            field=models.DateField(verbose_name=b'\xe8\xb4\xad\xe4\xb9\xa6\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
    ]
