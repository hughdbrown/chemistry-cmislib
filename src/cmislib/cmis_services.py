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
Module containing the base Binding class and other service objects.
"""
from exceptions import CmisException, RuntimeException, \
    ObjectNotFoundException, InvalidArgumentException, \
    PermissionDeniedException, NotSupportedException, \
    UpdateConflictException

class Binding(object):
    exceptions = {
        '400': InvalidArgumentException,
        '401': PermissionDeniedException,
        '403': PermissionDeniedException,
        '404': ObjectNotFoundException,
        '405': NotSupportedException,
        '409': UpdateConflictException,
        '500': RuntimeException,
    }

    def getRepositoryService(self):
        pass

    def _processCommonErrors(self, error, url):

        """
        Maps HTTPErrors that are common to all to exceptions. Only errors
        that are truly global, like 401 not authorized, should be handled
        here. Callers should handle the rest.
        """
        status = error['status']
        exception = Binding.exceptions.get(status, CmisException)
        raise exception(status, url)


class RepositoryServiceIfc(object):
    def getRepositories(self, client):
        pass

    def getRepositoryInfo(self):
        pass
