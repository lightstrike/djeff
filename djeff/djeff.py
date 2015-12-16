import re
from django.template.backends.django import DjangoTemplates, Template
from django.template.engine import _dirs_undefined

try:
    from html.parser import HTMLParser
except ImportError:
    from HTMLParser import HTMLParser


class DjeffTemplates(DjangoTemplates):
    def get_template(self, template_name, dirs=_dirs_undefined):
        return DjeffTemplate(self.engine.get_template(template_name, dirs))


class DjeffTemplate(Template):
    def render(self, context=None, request=None):
        rendered_context = super().render(context, request)
        return djeffify_html(rendered_context)


def djeffify_string(string_to_djeff):
    """
    Djeffifies string_to_djeff
    """
    string_to_djeff = re.sub(r'^(?=[jg])', 'd', string_to_djeff, flags=re.IGNORECASE)  # first
    string_to_djeff = re.sub(r'[ ](?=[jg])', ' d', string_to_djeff, flags=re.IGNORECASE)  # spaces
    string_to_djeff = re.sub(r'[\n](?=[jg])', '\nd', string_to_djeff, flags=re.IGNORECASE)  # \n
    return string_to_djeff


def djeffify_html(rendered_string):
    """
    This function contains the core logic for a
    middleware, template tag or Template engine approach
    """
    parser = DjeffParser()
    parser.feed(rendered_string)
    return parser.djhtml


def reconstruct_attrs(attrs):
    tag_string = ''
    for attr in attrs:
        tag_string += ('{}={} ').format(attr[0], attr[1])
    return tag_string.strip()


class DjeffParser(HTMLParser):
    def __init__(self, convert_charrefs=True, *args, **kwargs):
        """
        Explicitly set convert_charrefs to keep deprecation warnings at bay.

        See:
        https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser
        """
        # python 3
        try:
            HTMLParser.__init__(self, convert_charrefs=convert_charrefs)
        # python 2
        except TypeError:
            HTMLParser.__init__(self)
        self.djhtml = ''

    def handle_starttag(self, tag, attrs):
        self.djhtml += '<{} {}>'.format(tag, reconstruct_attrs(attrs))

    def handle_endtag(self, tag):
        self.djhtml += '</{}>'.format(tag)

    def handle_data(self, data):
        """
        Djeffify data between tags
        """
        if data.strip():
            data = djeffify_string(data)
        self.djhtml += data
