import io
from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-markwhat',
    version=".".join(map(str, __import__('django_markwhat').__version__)),
    packages=['django_markwhat', 'django_markwhat.templatetags'],
    url='http://pypi.python.org/pypi/django-markwhat',
    license="BSD-3-Clause",
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    install_requires=['Django', ],
    description="A collection of template filters that implement " +
            "common markup languages.",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    keywords=[
        'django',
        'markdown',
        'markup',
        'textile',
        'rst',
        'reStructuredText',
        'docutils',
        'commonmark',
        'web'
    ],
    platforms='OS Independent',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
)
