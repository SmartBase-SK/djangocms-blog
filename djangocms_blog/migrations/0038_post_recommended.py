# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-22 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0037_post_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='recommended',
            field=models.BooleanField(default=False, verbose_name='Recommended'),
        ),
    ]