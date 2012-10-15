import time
import urlparse
import urllib
import httplib2
try:
    import json
except ImportError:
    import simplejson as json

# Python 2.5 compat fix
if not hasattr(urlparse, 'parse_qsl'):
    import cgi
    urlparse.parse_qsl = cgi.parse_qsl

import razorapi
from razorapi import exceptions

class RazorApiClient(httplib2.Http):
    
    USER_AGENT = 'python-razorclient/%s' % razorapi.__version__
    
    def __init__(self, ip, port=8026):
        super(RazorApiClient, self).__init__()

        self.url = 'http://%s:%s/razor/api' % (ip, port)
        
        # httplib2 overrides
        self.force_exception_to_status_code = True

    def request(self, *args, **kwargs):
        kwargs.setdefault('headers', {})
        kwargs['headers']['User-Agent'] = self.USER_AGENT
        if 'body' in kwargs:
            kwargs['headers']['Content-Type'] = 'application/json'
            kwargs['body'] = json.dumps(kwargs['body'])
            
        resp, body = super(RazorApiClient, self).request(*args, **kwargs)
        if body:
            body = json.loads(body)
        else:
            body = None

        if resp.status in (400, 401, 403, 404, 413, 500):
            raise exceptions.from_response(resp, body)

        return resp, body

    def _razor_request(self, url, method, **kwargs):

        # Perform the request once. If it fails try it again. If it failes
        # twice then raise the exception
        try:
            resp, body = self.request(self.url + url, method, **kwargs)
            return resp, body
        except exceptions.Unauthorized, ex:
            try:
                resp, body = self.request(self.url + url, method, **kwargs)
                return resp, body
            except exceptions.Unauthorized:
                raise ex

    def get(self, url, **kwargs):
        return self._razor_request(url, 'GET', **kwargs)
    
    def post(self, url, **kwargs):
        return self._razor_request(url, 'POST', **kwargs)
    
    def put(self, url, **kwargs):
        return self._razor_request(url, 'PUT', **kwargs)
    
    def delete(self, url, **kwargs):
        return self._razor_request(url, 'DELETE', **kwargs)