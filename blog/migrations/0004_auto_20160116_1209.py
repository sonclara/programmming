# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 03:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160115_1916'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='cate',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_category',
            new_name='cate',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
    ]