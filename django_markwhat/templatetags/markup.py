"""
Set of "markup" template filters for Django.
These filters transform plain text
markup syntaxes to HTML; currently there is support for:

    * Textile, which requires the PyTextile library available at
      http://loopcore.com/python-textile/

    * Markdown, which requires the Python-markdown library from
      http://www.freewisdom.org/projects/python-markdown

    * reStructuredText, which requires docutils from http://docutils.sf.net/
"""

import warnings

from django import template
from django.conf import settings
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
def textile(value):
    """
    textile(is_safe=True)
    =====================
    """
    import textile

    return mark_safe(force_unicode(
        textile.textile(smart_str(value), encoding='utf-8', output='utf-8'))
    )

@register.filter(is_safe=True)
def markdown(value, args=''):
    """
    markdown(value, args='')
    ========================

    Runs Markdown over a given value, optionally using various
    extensions python-markdown supports.

    Syntax::

        {{ value|markdown:"extension1_name,extension2_name..." }}

    To enable safe mode, which strips raw HTML and only returns HTML
    generated by actual Markdown syntax, pass "safe" as the first
    extension in the list.

    If the version of Markdown in use does not support extensions,
    they will be silently ignored.

    """
    import markdown

    extensions = [e for e in args.split(',') if e]
    if len(extensions) > 0 and extensions[0] == "safe":
        extensions = extensions[1:]
        safe_mode = True
    else:
        safe_mode = False

    if safe_mode:
        return mark_safe(
            markdown.markdown(
                force_unicode(value),
                extensions,
                safe_mode=safe_mode,
                enable_attributes=False
            )
        )
    else:
        return mark_safe(
            markdown.markdown(
                force_unicode(value),
                extensions,
                safe_mode=safe_mode
            )
        )

@register.filter(is_safe=True)
def restructuredtext(value):
    """
    restructuredtext(value)
    =======================
    """
    from docutils.core import publish_parts

    docutils_settings = getattr(
        settings,
        "RESTRUCTUREDTEXT_FILTER_SETTINGS",
        {}
    )
    parts = publish_parts(
        source=smart_str(value),
        writer_name="html4css1",
        settings_overrides=docutils_settings
    )
    return mark_safe(force_unicode(parts["fragment"]))
