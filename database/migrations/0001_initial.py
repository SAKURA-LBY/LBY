# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-11-11 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_bookinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField()),
                ('bcomment', models.IntegerField()),
                ('isDelete', models.IntegerField(max_length=1)),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
                'db_table': 'book_bookinfo',
            },
        ),
        migrations.CreateModel(
            name='book_heroinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.IntegerField(max_length=1)),
                ('isDelete', models.IntegerField(max_length=1)),
                ('hcontent', models.CharField(max_length=200)),
                ('hbook_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.book_bookinfo')),
            ],
            options={
                'verbose_name': '英雄',
                'verbose_name_plural': '英雄',
                'db_table': 'book_heroinfo',
            },
        ),
    ]