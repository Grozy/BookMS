# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0021_auto_20151117_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookborrow',
            name='borrow_by_user',
            field=models.ForeignKey(verbose_name=b'\xe5\x80\x9f\xe9\x98\x85\xe8\x80\x85', to='BOOKMS.UserBaseInfo'),
            preserve_default=True,
        ),
    ]
