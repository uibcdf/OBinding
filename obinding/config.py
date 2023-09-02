# Configuration file for OBinding

# Set this variable true while testing
_testing = False

# Set this variable true while debugging
_debugging = False

# Sphinx

## Is sphinx working?
from os import environ
_sphinx_is_working = ('SPHINXWORKING' in environ)
del(environ)

# NGLview
_view_from_htmlfiles=False
if _sphinx_is_working:
    _view_from_htmlfiles=True

