from HTMLParser import HTMLParser


def reconstruct_attrs(attrs):
    tag_string = ''
    for attr in attrs:
        tag_string += (attr[0] + '=' + attr[1] + ' ')
    return tag_string.strip()


class DjeffParser(HTMLParser):
    text = ''

    def handle_starttag(self, tag, attrs):
        self.text += ('<%s %s>' % (tag, reconstruct_attrs(attrs)))

    def handle_endtag(self, tag):
        self.text += ('</%s>' % tag)

    def handle_data(self, data):
        data = data.replace(' G', ' dj')
        self.text += data


def djeff(string):
    parser = DjeffParser()
    parser.feed(string)
    return parser.text
