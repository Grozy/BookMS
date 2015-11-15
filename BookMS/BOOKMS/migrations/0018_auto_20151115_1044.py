# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0017_auto_20151115_0815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbaseinfo',
            old_name='account',
            new_name='user_account',
        ),
        migrations.RenameField(
            model_name='userbaseinfo',
            old_name='avator_url',
            new_name='user_avator_url',
        ),
        migrations.RenameField(
            model_name='userbaseinfo',
            old_name='uid',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='userbaseinfo',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='userbaseinfo',
            old_name='password',
            new_name='user_password',
        ),
    ]
