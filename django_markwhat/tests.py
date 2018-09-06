# Quick tests for the markup templatetags (django_markwhat)
import re
import unittest

from django.template import Template, Context
from django.utils.html import escape

try:
    import textile
except ImportError:
    textile = None

try:
    import markdown

    markdown_version = getattr(markdown, "version_info", 0)
except ImportError:
    markdown = None

try:
    import commonmark
except ImportError:
    commonmark = None

try:
    import docutils
except ImportError:
    docutils = None


class Templates(unittest.TestCase):
    textile_content = """Paragraph 1

Paragraph 2 with "quotes" and @code@"""

    markdown_content = """Paragraph 1

## An h2"""

    markdown_content_with_html_code = """Paragraph 1

## An h2

```
    <video width="320" height="240" controls>
        <source src="movie.mp4" type="video/mp4">
        <source src="movie.ogg" type="video/ogg">
    </video>
```
"""

    markdown_content_with_iframe_code = """Paragraph 1

## An h2

```
    <iframe src="http://example.com"></iframe>
```
"""

    rest_content = """Paragraph 1

Paragraph 2 with a link_

.. _link: http://www.example.com/"""

    @unittest.skipUnless(textile, 'texttile not installed')
    def test_textile(self):
        t = Template("{% load markup %}{{ textile_content|textile }}")
        rendered = t.render(Context(
            {'textile_content': self.textile_content})).strip()
        self.assertEqual(rendered.replace('\t', ''), """<p>Paragraph 1</p>

<p>Paragraph 2 with &#8220;quotes&#8221; and <code>code</code></p>""")

    @unittest.skipIf(textile, 'texttile is installed')
    def test_no_textile(self):
        t = Template("{% load markup %}{{ textile_content|textile }}")
        rendered = t.render(Context(
            {'textile_content': self.textile_content})).strip()
        self.assertEqual(rendered, escape(self.textile_content))

    @unittest.skipUnless(markdown, 'markdown not installed')
    def test_markdown(self):
        t = Template("{% load markup %}{{ markdown_content|markdown }}")
        rendered = t.render(Context({
            'markdown_content': self.markdown_content
        })).strip()
        pattern = re.compile("""<p>Paragraph 1\s*</p>\s*<h2>\s*An h2</h2>""")
        self.assertTrue(pattern.match(rendered))

    @unittest.skipUnless(markdown, 'markdown not installed')
    def test_markdown_html_code(self):
        t = Template("{% load markup %}{{ markdown_content|markdown }}")
        rendered = t.render(Context({
            'markdown_content': self.markdown_content_with_html_code
        })).strip()
        pattern = re.compile(
            '<p>Paragraph 1\s*</p>\s*<h2>\s*An h2</h2>' +
            '\s*<p><code>\s*&lt;video width="320"'
        )
        self.assertTrue(pattern.match(rendered))

    @unittest.skipUnless(markdown, 'markdown not installed')
    def test_markdown_html_iframe_code(self):
        t = Template("{% load markup %}{{ markdown_content|markdown }}")
        rendered = t.render(Context({
            'markdown_content': self.markdown_content_with_iframe_code
        })).strip()
        pattern = re.compile(
            '<p>Paragraph 1\s*</p>\s*<h2>\s*An h2</h2>' +
            '\s*<p><code>\s*&lt;iframe src="http://example.com"&gt;' +
            '&lt;/iframe&gt;'
        )
        self.assertTrue(pattern.match(rendered))

    @unittest.skipUnless(
        markdown and markdown_version >= (2, 1),
        'markdown >= 2.1 not installed'
    )
    def test_markdown_attribute_disable(self):
        t = Template("{% load markup %}{{ markdown_content|markdown:'safe' }}")
        markdown_content = "{@onclick=alert('hi')}some paragraph"
        rendered = t.render(Context(
            {'markdown_content': markdown_content})).strip()
        self.assertTrue('@' in rendered)

    @unittest.skipUnless(
        markdown and markdown_version >= (2, 1),
        'markdown >= 2.1 not installed'
    )
    def test_markdown_attribute_enable(self):
        t = Template("{% load markup %}{{ markdown_content|markdown }}")
        markdown_content = "{@onclick=alert('hi')}some paragraph"
        rendered = t.render(Context(
            {'markdown_content': markdown_content})).strip()
        self.assertFalse('@' in rendered)

    @unittest.skipIf(markdown, 'markdown is installed')
    def test_no_markdown(self):
        t = Template("{% load markup %}{{ markdown_content|markdown }}")
        rendered = t.render(Context(
            {'markdown_content': self.markdown_content})).strip()
        self.assertEqual(rendered, self.markdown_content)

    @unittest.skipUnless(commonmark, 'commonmark not installed')
    def test_commonmark(self):
        t = Template("{% load markup %}{{ markdown_content|commonmark }}")
        rendered = t.render(
            Context({'markdown_content': self.markdown_content})).strip()
        pattern = re.compile("""<p>Paragraph 1\s*</p>\s*<h2>\s*An h2</h2>""")
        self.assertTrue(pattern.match(rendered))

    @unittest.skipUnless(commonmark, 'commonmark not installed')
    def test_commonmark_html_code(self):
        t = Template("{% load markup %}{{ markdown_content|commonmark }}")
        rendered = t.render(Context({
            'markdown_content': self.markdown_content_with_html_code
        })).strip()
        pattern = re.compile(
            '<p>Paragraph 1\s*</p>\s*<h2>\s*An h2</h2>' +
            '\s*<pre><code>\s*&lt;video width=&quot;320&quot'
        )
        self.assertTrue(pattern.match(rendered))

    @unittest.skipUnless(commonmark, 'commonmark not installed')
    def test_commonmark_html_iframe_code(self):
        t = Template("{% load markup %}{{ markdown_content|commonmark }}")
        rendered = t.render(Context({
            'markdown_content': self.markdown_content_with_iframe_code
        })).strip()
        pattern = re.compile(
            '<p>Paragraph 1\s*</p>\s*<h2>\s*An h2</h2>' +
            '\s*<pre><code>\s*&lt;iframe ' +
            'src=&quot;http://example.com&quot;&gt;' +
            '&lt;/iframe&gt;'
        )
        self.assertTrue(pattern.match(rendered))

    @unittest.skipUnless(commonmark, 'commonmark not installed')
    def test_commonmark_empty_str(self):
        t = Template("{% load markup %}{{ markdown_content|commonmark }}")
        rendered = t.render(Context({'markdown_content': ''})).strip()
        self.assertEqual(rendered, '')

    @unittest.skipUnless(commonmark, 'commonmark not installed')
    def test_commonmark_none(self):
        t = Template("{% load markup %}{{ markdown_content|commonmark }}")
        rendered = t.render(Context({'markdown_content': None})).strip()
        self.assertEqual(rendered, '<p>None</p>')

    @unittest.skipUnless(docutils, 'docutils not installed')
    def test_docutils(self):
        t = Template("{% load markup %}{{ rest_content|restructuredtext }}")
        rendered = t.render(Context({
            'rest_content': self.rest_content
        })).strip()
        # Different versions of docutils return slightly different HTML
        try:
            # Docutils v0.4 and earlier
            self.assertEqual(
                rendered,
                '<p>Paragraph 1</p>\n' +
                '<p>Paragraph 2 with a <a class="reference" ' +
                'href="http://www.example.com/">link</a></p>')
        except AssertionError:
            # Docutils from SVN (which will become 0.5)
            self.assertEqual(
                rendered,
                '<p>Paragraph 1</p>\n' +
                '<p>Paragraph 2 with a ' +
                '<a class="reference external" ' +
                'href="http://www.example.com/">link</a></p>')

    @unittest.skipIf(docutils, 'docutils is installed')
    def test_no_docutils(self):
        t = Template("{% load markup %}{{ rest_content|restructuredtext }}")
        rendered = t.render(
            Context({'rest_content': self.rest_content})).strip()
        self.assertEqual(rendered, self.rest_content)
