from setuptools import setup

setup(
    name='django-markwhat',
    version=".".join(map(str, __import__('django_markwhat').__version__)),
    packages=['django_markwhat', 'django_markwhat.templatetags'],
    url='http://pypi.python.org/pypi/django-markwhat',
    license=open('LICENSE').read(),
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    install_requires=['Django', ],
    description="A collection of template filters that implement " + \
            "common markup languages.",
    long_description=open('README.rst').read(),
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
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
)
