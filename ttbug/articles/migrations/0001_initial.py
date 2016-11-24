# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blocks', '0002_auto_20161122_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('author', models.CharField(max_length=100, verbose_name='文章作者')),
                ('content', models.TextField(max_length=10000, verbose_name='文章内容')),
                ('create_time_stamp', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_update_timestamp', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blocks.Blocks', verbose_name='所属板块')),
            ],
            options={
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
    ]