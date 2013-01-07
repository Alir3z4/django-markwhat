=====================
Django MarkWhat
=====================

.. note::

    Extracted from `Django 1.4 since markup deprecation <https://docs.djangoproject.com/en/dev/releases/1.5/#django-contrib-markup>`_

------

A collection of template filters that implement common markup languages.

provides template filters that implement the following markup
languages:

* ``textile`` -- implements `Textile`_ -- requires `PyTextile`_
* ``markdown`` -- implements `Markdown`_ -- requires `Python-markdown`_
* ``restructuredtext`` -- implements `reST (reStructured Text)`_
  -- requires `doc-utils`_

In each case, the filter expects formatted markup as a string and
returns a string representing the marked-up text. For example, the
``textile`` filter converts text that is marked-up in Textile format
to HTML.

Installation
------------
``django-markwhat`` is available on pypi:

http://pypi.python.org/pypi/django-markwhat

So easily install it by ``pip``:
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
.. _reST (reStructured Text): http://en.wikipedia.org/wiki/ReStructuredText
.. _PyTextile: http://loopcore.com/python-textile/
.. _Python-markdown: http://pypi.python.org/pypi/Markdown
.. _doc-utils: http://docutils.sf.net/

reStructured Text
-----------------

When using the ``restructuredtext`` markup filter you can define a
`RESTRUCTUREDTEXT_FILTER_SETTINGS` in your django settings to
override the default writer settings. See the `restructuredtext writer
settings`_ for details on what these settings are.

.. warning::

   reStructured Text has features that allow raw HTML to be included, and that
   allow arbitrary files to be included. These can lead to XSS vulnerabilities
   and leaking of private information. It is your responsibility to check the
   features of this library and configure appropriately to avoid this. See the
   `Deploying Docutils Securely
   <http://docutils.sourceforge.net/docs/howto/security.html>`_ documentation.

.. _restructuredtext writer settings: http://docutils.sourceforge.net/docs/user/config.html#html4css1-writer

Markdown
--------

The Python Markdown library supports options named "safe_mode" and
"enable_attributes". Both relate to the security of the output. To enable both
options in tandem, the markdown filter supports the "safe" argument.
::
    
    { markdown_content_var|markdown:"safe" }}

.. warning::

    Versions of the Python-Markdown library prior to 2.1 do not support the
    optional disabling of attributes and by default

