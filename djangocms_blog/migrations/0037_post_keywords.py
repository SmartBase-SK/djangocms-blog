# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-12 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0036_auto_20170912_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.CharField(blank=True, help_text='Page meta keywords', max_length=400, null=True, verbose_name='Keywords'),
        ),
    ]
