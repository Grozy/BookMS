# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0007_auto_20151112_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_borrow_status',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6\xe5\x80\x9f\xe9\x98\x85\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
    ]
