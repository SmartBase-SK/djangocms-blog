# Generated by Django 2.1.9 on 2020-04-21 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0044_auto_20190626_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('url', models.URLField()),
                ('short_text', models.CharField(max_length=400)),
                ('button_text', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'ordering': ('-date_created',),
                'verbose_name_plural': 'calls to action',
                'verbose_name': 'call to action',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='call_to_action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_post_cta', to='djangocms_blog.CallToAction', verbose_name='Call to Action'),
        ),
    ]