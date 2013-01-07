from distutils.core import setup

setup(
    name='django-markwhat',
    version=".".join(map(str, __import__('django_markwhat').__version__)),
    packages=['django_markwhat', 'django_markwhat.templatetags'],
    url='http://pypi.python.org/pypi/django-markwhat',
    license=open('LICENSE').read(),
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    install_requires=['django',],
    description='A collection of template filters that implement common markup languages.',
    long_description=open('README.rst').read(),
    keywords=[
        'django',
        'markdown',
        'markup',
        'textile',
        'rst',
        'reStructuredText',
        'docutils',
        'web'
    ],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development'
    ],
)
