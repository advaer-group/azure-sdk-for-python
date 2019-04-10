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

from .tracked_resource import TrackedResource


class Cluster(TrackedResource):
    """Single Event Hubs Cluster resource in List or Get operations.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku: Properties of the cluster SKU.
    :type sku: ~azure.mgmt.eventhub.v2018_01_01_preview.models.ClusterSku
    :ivar created: The UTC time when the Event Hubs Cluster was created.
    :vartype created: str
    :ivar updated: The UTC time when the Event Hubs Cluster was last updated.
    :vartype updated: str
    :ivar metric_id: The metric ID of the cluster resource. Provided by the
     service and not modifiable by the user.
    :vartype metric_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created': {'readonly': True},
        'updated': {'readonly': True},
        'metric_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'ClusterSku'},
        'created': {'key': 'properties.created', 'type': 'str'},
        'updated': {'key': 'properties.updated', 'type': 'str'},
        'metric_id': {'key': 'properties.metricId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Cluster, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.created = None
        self.updated = None
        self.metric_id = None
