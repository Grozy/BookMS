# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKMS', '0010_auto_20151115_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_id', models.IntegerField(verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6\xe7\xbc\x96\xe5\x8f\xb7')),
                ('uid', models.IntegerField(verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5\xe7\xbc\x96\xe5\x8f\xb7')),
                ('borrow_time', models.DateField(verbose_name=b'\xe5\x80\x9f\xe9\x98\x85\xe6\x97\xa5\xe6\x9c\x9f')),
                ('is_over_time', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xb6\x8a\xe6\x9c\x9f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserTypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField(verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5\xe7\xbc\x96\xe5\x8f\xb7')),
                ('user_type', models.CharField(default=b'', max_length=1, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='userbaseinfo',
            name='avator_url',
            field=models.TextField(verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
            preserve_default=True,
        ),
    ]
