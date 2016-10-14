'''
AWS Auth plugin for HTTPie.
'''

__version__ = '0.1.0'
__author__ = 'Gabriel Majivu'
__licence__ = 'MIT'

from httpie.plugins import AuthPlugin
from requests_aws4auth import AWS4Auth

print 'batman!'

class AWSAuthPlugin(AuthPlugin):

    name = 'AWS Auth Plugin'
    description = 'Simple HTTPie plugin to help with signed AWS requests.'
    auth_type = 'awsauth'

    def get_auth(self, access_id, access_key, region, aws_service):
        return AWS4Auth(access_id, access_key, region, aws_service)
