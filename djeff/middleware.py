from django.conf import settings
from djeff import djeff
from django.core.exceptions import ImproperlyConfigured


class DjeffMiddleware(object):

    def process_response(self, request, response):
        try:
            if settings.DJEFF:
                response.content = djeff(response.content)
        except AttributeError:
            raise ImproperlyConfigured(
                'DJEFF is not configured in django settings. Set "DJEFF = True" to enable djeffing'
            )

        return response
