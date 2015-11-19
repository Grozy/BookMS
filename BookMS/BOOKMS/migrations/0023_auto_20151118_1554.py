# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0022_auto_20151118_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookborrow',
            name='book',
            field=models.ForeignKey(verbose_name=b'\xe4\xb9\xa6\xe5\x90\x8d', to='BOOKMS.Book'),
            preserve_default=True,
        ),
    ]
