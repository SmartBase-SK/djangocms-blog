# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-26 12:31
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0028_auto_20170304_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='main_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_category_image', to='filer.Image', verbose_name='category main image'),
        ),
    ]
