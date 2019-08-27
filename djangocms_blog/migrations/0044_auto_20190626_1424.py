# Generated by Django 2.1.9 on 2019-06-26 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0043_merge_20190626_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorentriesplugin',
            name='authors',
            field=models.ManyToManyField(limit_choices_to={'djangocms_blog_post_author__publish': True}, to=settings.AUTH_USER_MODEL, verbose_name='authors'),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='main_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Blog category image'),
        ),
        migrations.AlterField(
            model_name='latestpostsplugin',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Show only the blog articles tagged with chosen tags.', related_name='djangocms_blog_latest_post', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='filter by tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='djangocms_blog_tags', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]