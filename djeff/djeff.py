from django.template.backends.django import DjangoTemplates, Template
from django.template.engine import _dirs_undefined
from html.parser import HTMLParser


class DjeffTemplates(DjangoTemplates):
    def get_template(self, template_name, dirs=_dirs_undefined):
        return DjeffTemplate(self.engine.get_template(template_name, dirs))


class DjeffTemplate(Template):
    def render(self, context=None, request=None):
        rendered_context = super().render(context, request)
        return djeffify(rendered_context)


def djeffify(rendered_string):
    """
    This function contains the core logic for a
    middleware, template tag or Template engine approach
    """
    parser = DjeffParser()
    parser.feed(rendered_string)
    return parser.dhtml


def reconstruct_attrs(attrs):
    tag_string = ''
    for attr in attrs:
        tag_string += (attr[0] + '=' + attr[1] + ' ')
    return tag_string.strip()


class DjeffParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs)
        self.dhtml = ''

    def handle_starttag(self, tag, attrs):
        self.dhtml += '<{} {}>'.format(tag, reconstruct_attrs(attrs))

    def handle_endtag(self, tag):
        self.dhtml += '</{}>'.format(tag)

    def handle_data(self, data):
        """
        FIXME: Add more functionality!
        """
        if data.strip():
            data = "d{}".format(data)
        self.dhtml += data

