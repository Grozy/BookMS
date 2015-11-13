# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='book_title',
        ),
    ]
