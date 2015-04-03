"""
Running tests for django without using django-admin.py
Or using manage.py.
Basically run just by executing this file.

Thanks to:
    - http://stackoverflow.com/q/3841725/636136
    - http://stackoverflow.com/a/3851333/636136
    - http://stackoverflow.com/a/12260597/636136

"""
import os
import sys
import django
from django.conf import settings
from django.core.management import call_command

DJANGO_VERSION = float('.'.join([str(i) for i in django.VERSION[0:2]]))

DIR_NAME = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django_markwhat'
    ),
    MIDDLEWARE_CLASSES=[],
)

if DJANGO_VERSION >= 1.7:
    django.setup()

call_command('test')
