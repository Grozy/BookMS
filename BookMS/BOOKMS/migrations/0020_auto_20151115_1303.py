# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0019_auto_20151115_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookborrow',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='borrowhistory',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='borrowhistory',
            name='uid',
        ),
        migrations.AddField(
            model_name='bookborrow',
            name='book',
            field=models.ForeignKey(default=1, to='BOOKMS.Book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookborrow',
            name='borrow_by_user',
            field=models.ForeignKey(default=1, to='BOOKMS.UserBaseInfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='borrowhistory',
            name='book',
            field=models.ForeignKey(default=1, to='BOOKMS.Book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='borrowhistory',
            name='user',
            field=models.ForeignKey(default=1, to='BOOKMS.UserBaseInfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usertypeinfo',
            name='uid',
            field=models.ForeignKey(to='BOOKMS.UserBaseInfo'),
            preserve_default=True,
        ),
    ]
