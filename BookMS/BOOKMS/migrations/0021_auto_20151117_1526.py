# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0020_auto_20151115_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertypeinfo',
            old_name='uid',
            new_name='user',
        ),
    ]
