# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class ResponseWithError(Model):
    """An error response from the API.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. Error information.
    :type error: ~azure.mgmt.monitor.models.Error
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(self, *, error, **kwargs) -> None:
        super(ResponseWithError, self).__init__(**kwargs)
        self.error = error


class ResponseWithErrorException(HttpOperationError):
    """Server responsed with exception of type: 'ResponseWithError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ResponseWithErrorException, self).__init__(deserialize, response, 'ResponseWithError', *args)
