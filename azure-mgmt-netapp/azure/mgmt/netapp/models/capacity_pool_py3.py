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


class CapacityPool(Model):
    """Capacity pool resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: object
    :ivar pool_id: poolId. UUID v4 used to identify the Pool
    :vartype pool_id: str
    :param size: size. Provisioned size of the pool (in bytes). Allowed values
     are in 4TiB chunks (value must be multiply of 4398046511104). Default
     value: 4398046511104 .
    :type size: long
    :param service_level: serviceLevel. The service level of the file system.
     Possible values include: 'Standard', 'Premium', 'Ultra'. Default value:
     "Premium" .
    :type service_level: str or ~azure.mgmt.netapp.models.ServiceLevel
    :ivar provisioning_state: Azure lifecycle management
    :vartype provisioning_state: str
    """

    _validation = {
        'location': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'pool_id': {'readonly': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'size': {'maximum': 549755813888000, 'minimum': 4398046511104},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
        'pool_id': {'key': 'properties.poolId', 'type': 'str'},
        'size': {'key': 'properties.size', 'type': 'long'},
        'service_level': {'key': 'properties.serviceLevel', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, size: int=4398046511104, service_level="Premium", **kwargs) -> None:
        super(CapacityPool, self).__init__(**kwargs)
        self.location = location
        self.id = None
        self.name = None
        self.type = None
        self.tags = tags
        self.pool_id = None
        self.size = size
        self.service_level = service_level
        self.provisioning_state = None
