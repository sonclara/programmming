# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 03:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160116_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cate',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='cate',
            new_name='category',
        ),
    ]
