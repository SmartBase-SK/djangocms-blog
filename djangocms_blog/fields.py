# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import django
from django.db.models import SlugField

__all__ = ['AutoSlugField']


class AutoSlugField(SlugField):
    def __init__(self, *args, **kwargs):
        super(AutoSlugField, self).__init__(*args, **kwargs)
