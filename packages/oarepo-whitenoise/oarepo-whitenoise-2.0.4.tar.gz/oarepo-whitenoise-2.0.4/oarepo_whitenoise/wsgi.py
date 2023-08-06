"""WhiteNoise bridge to flask app."""

import os

from oarepo_micro_api.wsgi import application as application
from whitenoise import WhiteNoise
from whitenoise.string_utils import decode_path_info

static_folder = os.environ.get('WHITENOISE_ROOT', '/whitenoise')

assert os.path.exists(static_folder)


API_ROUTES = [
    '/oauth'
]


class IndexWhiteNoise(WhiteNoise):
    """Modified whitenoise to serve index.html for any not-found url apart from api"""

    def __call__(self, environ, start_response):
        """Call api or whitenoise"""
        path = decode_path_info(environ.get("PATH_INFO", ""))

        if not any([path.startswith(r) for r in API_ROUTES]):
            if self.autorefresh:
                static_file = self.find_file(path)
            else:
                static_file = self.files.get(path)

            accept = environ.get('HTTP_ACCEPT', '')
            query = environ.get('QUERY_STRING', '')
            if static_file is None and 'html' in accept and not query == 'download':
                if self.autorefresh:
                    static_file = self.find_file('/index.html')
                else:
                    static_file = self.files.get('/index.html')
            if static_file:
                return self.serve(static_file, environ, start_response)

        return self.application(environ, start_response)

    def add_cache_headers(self, headers, path, url):
        """Adds no-store cache header to urls with mutable content."""
        if self.immutable_file_test(path, url):
            headers["Cache-Control"] = "max-age={0}, public, immutable".format(
                self.FOREVER
            )
        elif self.max_age is not None:
            headers["Cache-Control"] = "no-store"

    def immutable_file_test(self, path, url):
        """Returns Vue static asset urls as immutable."""
        return url.startswith('/js/') or \
            url.startswith('/css/') or \
            url.startswith('/img/') or \
            url.startswith('/fonts/')


application.wsgi_app = IndexWhiteNoise(application.wsgi_app, root=static_folder)
