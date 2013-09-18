#
#      Licensed to the Apache Software Foundation (ASF) under one
#      or more contributor license agreements.  See the NOTICE file
#      distributed with this work for additional information
#      regarding copyright ownership.  The ASF licenses this file
#      to you under the Apache License, Version 2.0 (the
#      "License"); you may not use this file except in compliance
#      with the License.  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#      Unless required by applicable law or agreed to in writing,
#      software distributed under the License is distributed on an
#      "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#      KIND, either express or implied.  See the License for the
#      specific language governing permissions and limitations
#      under the License.
#
"""
Module that takes care of network communications for cmislib. It does
not know anything about CMIS or do anything special with regard to the
response it receives.
"""

import logging
import requests


class RESTService(object):

    """
    Generic service for interacting with an HTTP end point. Sets headers
    such as the USER_AGENT and builds the basic auth handler.
    """

    def __init__(self):
        self.user_agent = 'cmislib/%s +http://chemistry.apache.org/'
        self.logger = logging.getLogger('cmislib.net.RESTService')

    def get_headers(self, headers, contentType=None):
        headers = headers or {}
        items = headers.items() + [('User-Agent', self.user_agent), ('Content-Type', contentType)]
        return dict(t for t in items if t[1])

    def get(self,
            url,
            username=None,
            password=None,
            payload=None,  # dict of url params
            headers=None,  # dict of additional headers
            **kwargs):     # additional parameters for requests

        """
        Makes a get request to the URL specified.
        """

        self.logger.debug('About to do a GET on: ' + url)
        return requests.get(url,
                            auth=(username, password),
                            headers=self.get_headers(headers),
                            payload=payload,
                            **kwargs)

    def delete(self,
               url,
               username=None,
               password=None,
               payload=None,  # dict of url params
               headers=None,  # dict of additional headers
               **kwargs):

        """
        Makes a delete request to the URL specified.
        """

        self.logger.debug('About to do a DELETE on: ' + url)
        return requests.delete(url,
                               auth=(username, password),
                               headers=self.get_headers(headers),
                               payload=payload,
                               **kwargs)

    def put(self,
            url,
            data,
            username=None,
            password=None,
            payload=None,
            contentType=None,
            headers=None,
            **kwargs):

        """
        Makes a PUT request to the URL specified and includes the payload
        that gets passed in. The content type header gets set to the
        specified content type.
        """

        self.logger.debug('About to do a PUT on: ' + url)
        return requests.put(url,
                            auth=(username, password),
                            headers=self.get_headers(headers, contentType),
                            data=data,
                            payload=payload,
                            **kwargs)

    def post(self,
             url,
             data,
             username=None,
             password=None,
             payload=None,
             contentType=None,
             headers=None,
             **kwargs):

        """
        Makes a POST request to the URL specified and posts the payload
        that gets passed in. The content type header gets set to the
        specified content type.
        """

        self.logger.debug('About to do a POST on:' + url)
        return requests.post(url,
                             auth=(username, password),
                             headers=self.get_headers(headers, contentType),
                             data=data,
                             payload=payload,
                             **kwargs)
