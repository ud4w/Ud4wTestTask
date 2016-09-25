"""Middleware who's fate is to collect the requests and store them in DB."""


class RequestCollectorMiddleware(object):
    """Class designed to collect requests."""

    def process_request(self, request):
        """Collecting requests here."""
        print request.META
