# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0014_auto_20151115_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbaseinfo',
            name='avator_url',
            field=models.TextField(verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True),
            preserve_default=True,
        ),
    ]
