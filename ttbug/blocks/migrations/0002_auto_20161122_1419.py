# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blocks',
            options={'verbose_name': '板块', 'verbose_name_plural': '板块'},
        ),
    ]
