=====================
Django MarkWhat
=====================

.. image:: https://travis-ci.org/Alir3z4/django-markwhat.svg?branch=master
    :target: https://travis-ci.org/Alir3z4/django-markwhat


.. contents:: Table of contents

.. note::

    Extracted from `Django 1.4 since markup deprecation <https://docs.djangoproject.com/en/dev/releases/1.5/#django-contrib-markup>`_

------

A collection of template filters that implement common markup languages.

provides template filters that implement the following markup
languages:

* ``textile`` -- implements `Textile`_ -- requires `PyTextile`_
* ``markdown`` -- implements `Markdown`_ -- requires `Python-markdown`_
* ``commonmark`` -- implements `CommonMark`_ -- requires `CommonMark-py`_
* ``reStructuredText`` -- implements `reStructuredText`_
  -- requires `docutils`_

In each case, the filter expects formatted markup as a string and
returns a string representing the marked-up text. For example, the
``textile`` filter converts text that is marked-up in Textile format
to HTML.


Supported Python versions
=========================

``django-crequest`` currently can be run on multiple python versions:

* Python 2 (2.7)
* Python 3 (3.5, 3.6, 3.7)
* PyPy



Installation
------------
``django-markwhat`` is available on pypi:

https://pypi.org/project/django-markwhat/

Install it by ``pip``:
::
    
    pip install django-markwhat

Or by ``easy_install``
::
    
    $ easy_install django-markwhat

Another way is by cloning ``django-markwhat``'s `git repo <https://github.com/Alir3z4/django-markwhat>`_ :::
    
    git clone git://github.com/Alir3z4/django-markwhat.git

Then install it by running:
::
    
    $ python setup.py install

Configuration
******************

To activate these filters, add ``'django_markwhat'`` to your
``INSTALLED_APPS`` setting. Once you've done that, use
``{% load markup %}`` in a template, and you'll have access to these filters.

.. warning::

    The output of markup filters is marked "safe" and will not be escaped when
    rendered in a template. Always be careful to sanitize your inputs and make
    sure you are not leaving yourself vulnerable to cross-site scripting or
    other types of attacks.

.. _Textile: http://en.wikipedia.org/wiki/Textile_%28markup_language%29
.. _Markdown: http://en.wikipedia.org/wiki/Markdown
.. _CommonMark: http://commonmark.org
.. _CommonMark-py: https://pypi.python.org/pypi/CommonMark
.. _reST (reStructured Text): http://en.wikipedia.org/wiki/reStructuredText
.. _PyTextile: http://loopcore.com/python-textile/
.. _Python-markdown: http://pypi.python.org/pypi/Markdown
.. _docutils: http://docutils.sf.net/

reStructuredText
----------------

When using the ``reStructuredText`` markup filter you can define a
`RESTRUCTUREDTEXT_FILTER_SETTINGS` in your django settings to
override the default writer settings. See the `reStructuredText writer
settings`_ for details on what these settings are.

.. warning::

   reStructuredText has features that allow raw HTML to be included, and that
   allow arbitrary files to be included. These can lead to XSS vulnerabilities
   and leaking of private information. It is your responsibility to check the
   features of this library and configure appropriately to avoid this. See the
   `Deploying Docutils Securely
   <http://docutils.sourceforge.net/docs/howto/security.html>`_ documentation.

.. _reStructuredText writer settings: http://docutils.sourceforge.net/docs/user/config.html#html4css1-writer

Markdown
--------

The Python Markdown library supports options named "safe_mode" and
"enable_attributes". Both relate to the security of the output. To enable both
options in tandem, the markdown filter supports the "safe" argument.
::
    
    {{ markdown_content_var|markdown:"safe" }}

.. warning::

    Versions of the Python-Markdown library prior to 2.1 do not support the
    optional disabling of attributes and by default

Tests
-----

``django-markwhat`` is tested on both `python2` and `python3`, to run the tests:

::

    $ python run_tests.py
