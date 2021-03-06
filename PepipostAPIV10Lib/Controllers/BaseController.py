# -*- coding: utf-8 -*-

"""
   PepipostAPIV10Lib

   This file was automatically generated by APIMATIC BETA v2.0 on 04/15/2016
"""

from PepipostAPIV10Lib.Http.RequestsClient import *
from PepipostAPIV10Lib.APIException import APIException

class BaseController(object):

    """All controllers inherit from this base class. It manages shared HTTP clients and global API errors."""

    http_client = RequestsClient()

    def __init__(self, client):
        if client != None:
            self.http_client = client

    def validate_response(self, response):
        if (response.status_code < 200) or (response.status_code > 206): #[200,206] = HTTP OK
            raise APIException("HTTP Response Not OK", response.status_code, response.raw_body)
