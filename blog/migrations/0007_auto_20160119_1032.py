# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160116_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
