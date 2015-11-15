# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0008_book_book_borrow_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookBorrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_id', models.IntegerField()),
                ('is_borrowed', models.BooleanField(default=False, verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6\xe5\x80\x9f\xe9\x98\x85\xe7\x8a\xb6\xe6\x80\x81')),
                ('book_borrowed_time', models.DateField(verbose_name=b'\xe8\xa2\xab\xe5\x80\x9f\xe9\x98\x85\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserBaseInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('uid', models.IntegerField()),
                ('account', models.CharField(max_length=30, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=16, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('avator_url', models.CharField(max_length=150, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f\xe5\x9c\xb0\xe5\x9d\x80')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='createTime',
            new_name='book_create_time',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_borrow_status',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_title',
        ),
        migrations.AddField(
            model_name='book',
            name='book_logo_url',
            field=models.CharField(default='', max_length=150, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_name',
            field=models.CharField(default='', max_length=150, verbose_name='\u4e66\u540d'),
            preserve_default=False,
        ),
    ]
