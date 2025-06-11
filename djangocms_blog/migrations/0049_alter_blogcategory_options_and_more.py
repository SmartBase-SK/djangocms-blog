from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0048_alter_authorentriesplugin_cmsplugin_ptr_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'ordering': ('order_by',), 'verbose_name': 'blog category', 'verbose_name_plural': 'blog categories'},
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='order_by',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='mostreadplugin',
            name='template_folder',
            field=models.CharField(choices=[('plugins', 'Default template'), ('blog_list', 'Blog list'), ('dark_bg', 'For dark background')], default='plugins', help_text='Select plugin template to load for this instance', max_length=200, verbose_name='Plugin template'),
        ),
    ]
