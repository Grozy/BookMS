# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0016_auto_20151115_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_ISBN',
            field=models.CharField(default=11, max_length=13, verbose_name=b'ISBN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(default=11, max_length=30, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_description',
            field=models.TextField(default=11, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9\xe7\xae\x80\xe4\xbb\x8b'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_paper_type',
            field=models.CharField(default=11, max_length=10, verbose_name=b'\xe7\xba\xb8\xe8\xb4\xa8'),
            preserve_default=False,
        ),
    ]
