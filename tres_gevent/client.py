from trhttp_gevent.rest.client import GRestClient
from tres.client import ESClient

class GESClient(ESClient):
    def __init__(
            self,
            endpoint,
            timeout=10,
            keepalive=True,
            rest_client_class=None):

        rest_client_class = rest_client_class or GRestClient

        super(GESClient, self).__init__(
                endpoint=endpoint,
                timeout=timeout,
                keepalive=keepalive,
                rest_client_class=rest_client_class)
