# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0015_auto_20151115_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbaseinfo',
            name='uid',
            field=models.IntegerField(verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5\xe7\xbc\x96\xe5\x8f\xb7'),
            preserve_default=True,
        ),
    ]
