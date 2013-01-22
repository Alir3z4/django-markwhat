"""
Running tests for django without using django-admin.py
Or using manage.py.
Bassically runnig just by executing this file.

Thanks to:
    - http://stackoverflow.com/q/3841725/636136
    - http://stackoverflow.com/a/3851333/636136
    - http://stackoverflow.com/a/12260597/636136

"""
import os
import sys
from django.conf import settings

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
    )
)

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['django_markwhat', ])
if failures:
    sys.exit(failures)
