# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import sys

from django.http import QueryDict

from djangocms_blog.models import BlogCategory

from .base import BaseTest


class WizardTest(BaseTest):

    def setUp(self):
        try:
            from cms.wizards.wizard_pool import wizard_pool
            delete = [
                'djangocms_blog',
                'djangocms_blog.cms_wizards',
            ]
            for module in delete:
                if module in sys.modules:
                    del sys.modules[module]
            wizard_pool._reset()
        except ImportError:
            # Not in django CMS 3.2+, no cleanup needed
            pass
        super(WizardTest, self).setUp()

    def get_querydict(self, source):
        tmp = QueryDict(mutable=True)
        tmp.update(source)
        tmp._mutable = False
        return tmp

    def test_wizard(self):
        """
        Test that Blog wizard is present and contains all items
        """
        from cms.wizards.wizard_pool import wizard_pool
        self.get_pages()

        titles = [entry.title for entry in wizard_pool.get_entries()]
        self.assertTrue('New Blog' in titles)
        self.assertTrue('New Article' in titles)

    def test_wizard_init(self):
        from cms.utils.permissions import current_user
        from cms.wizards.wizard_pool import wizard_pool
        from djangocms_blog.models import Post
        self.get_pages()

        cat_1 = BlogCategory.objects.create(name='category 1 - blog 1', app_config=self.app_config_1)
        cat_2 = BlogCategory.objects.create(name='category 1 - blog 2', app_config=self.app_config_2)
        cats = {
            self.app_config_1.pk: cat_1,
            self.app_config_2.pk: cat_2,
        }
        with current_user(self.user_staff):
            wizs = [entry for entry in wizard_pool.get_entries() if entry.model == Post]
            for index, wiz in enumerate(wizs):
                app_config = self.app_config_1.pk if wiz.title == 'New Blog' else self.app_config_2.pk
                form = wiz.form()
                self.assertTrue(form.initial.get('app_config', False), app_config)
                self.assertTrue(form.fields['app_config'].widget.attrs['disabled'])

                form = wiz.form(data=self.get_querydict({
                    '1-title': 'title{0}'.format(index),
                    '1-abstract': 'abstract{0}'.format(index),
                    '1-categories': cats[app_config].pk,
                }), prefix=1)
                self.assertEqual(form.default_appconfig, app_config)
                self.assertTrue(form.is_valid())
                self.assertEqual(form.cleaned_data['app_config'].pk, app_config)
                instance = form.save()
                self.assertEqual(instance.author, self.user_staff)

            with self.settings(BLOG_AUTHOR_DEFAULT='normal'):
                for index, wiz in enumerate(wizs):
                    app_config = self.app_config_1.pk if wiz.title == 'New Blog' else self.app_config_2.pk
                    form = wiz.form(data=self.get_querydict({
                        '1-title': 'title-2{0}'.format(index),
                        '1-abstract': 'abstract-2{0}'.format(index),
                        '1-categories': cats[app_config].pk,
                    }), prefix=1)
                    self.assertEqual(form.default_appconfig, app_config)
                    self.assertTrue(form.is_valid())
                    self.assertEqual(form.cleaned_data['app_config'].pk, app_config)
                    instance = form.save()
                    self.assertEqual(instance.author, self.user_normal)

    def test_wizard_duplicate_slug(self):
        from cms.utils.permissions import current_user
        from cms.wizards.wizard_pool import wizard_pool
        from djangocms_blog.models import Post
        self.get_pages()
        cat_2 = BlogCategory.objects.create(name='category 1 - blog 2', app_config=self.app_config_2)

        with current_user(self.user_staff):
            wiz = None
            for wiz in wizard_pool.get_entries():
                if wiz.model == Post and wiz.title == 'New Blog':
                    break
            form = wiz.form(data=self.get_querydict({
                '1-title': 'title article',
                '1-abstract': 'abstract article',
                '1-categories': self.category_1.pk,
            }), prefix=1)
            self.assertEqual(form.default_appconfig, self.app_config_1.pk)
            self.assertTrue(form.is_valid())
            instance1 = form.save()
            self.assertEqual(instance1.slug, 'title-article')

            form = wiz.form(data=self.get_querydict({
                '1-title': 'title article',
                '1-abstract': 'abstract article',
                '1-categories': self.category_1.pk,
            }), prefix=1)
            self.assertEqual(form.default_appconfig, self.app_config_1.pk)
            self.assertTrue(form.is_valid())
            instance2 = form.save()
            self.assertEqual(instance2.slug, 'title-article-1')

            for wiz in wizard_pool.get_entries():
                if wiz.model == Post and wiz.title == 'New Article':
                    break
            form = wiz.form(data=self.get_querydict({
                '1-title': 'title article',
                '1-abstract': 'abstract article',
                '1-categories': cat_2.pk,
            }), prefix=1)
            self.assertEqual(form.default_appconfig, self.app_config_2.pk)
            self.assertTrue(form.is_valid())
            instance3 = form.save()
            self.assertEqual(instance3.slug, 'title-article-2')

    def test_wizard_init_categories_check(self):
        from cms.utils.permissions import current_user
        from cms.wizards.wizard_pool import wizard_pool
        from djangocms_blog.models import Post
        self.get_pages()

        with current_user(self.user_staff):
            wiz = None
            for wiz in wizard_pool.get_entries():
                if wiz.model == Post and wiz.title == 'New Article':
                    break
            form = wiz.form(data=self.get_querydict({
                '1-title': 'title article',
                '1-abstract': 'abstract article',
                '1-categories': self.category_1.pk,
            }), prefix=1)
            self.assertEqual(form.default_appconfig, self.app_config_2.pk)
            self.assertFalse(form.is_valid())
            self.assertTrue('categories' in form.errors.keys())

    def test_wizard_import(self):
        # The following import should not fail in any django CMS version
        pass
