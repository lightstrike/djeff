========
Usage
========

To use Djeff in a project::

* To use as middleware
djeff all your responses by adding the following lines to your settings.py::

    MIDDLEWARE_CLASSES = (
        ...,
        'djeff.middleware.DjeffMiddleware',
    )
    
    DJEFF = True
