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

from .resource import Resource


class ExpressRouteGateway(Resource):
    """ExpressRoute gateway resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param auto_scale_configuration: Configuration for auto scaling.
    :type auto_scale_configuration:
     ~azure.mgmt.network.v2019_02_01.models.ExpressRouteGatewayPropertiesAutoScaleConfiguration
    :ivar express_route_connections: List of ExpressRoute connections to the
     ExpressRoute gateway.
    :vartype express_route_connections:
     list[~azure.mgmt.network.v2019_02_01.models.ExpressRouteConnection]
    :param provisioning_state: The provisioning state of the resource.
     Possible values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :type provisioning_state: str or
     ~azure.mgmt.network.v2019_02_01.models.ProvisioningState
    :param virtual_hub: Required. The Virtual Hub where the ExpressRoute
     gateway is or will be deployed.
    :type virtual_hub: ~azure.mgmt.network.v2019_02_01.models.VirtualHubId
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'express_route_connections': {'readonly': True},
        'virtual_hub': {'required': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'auto_scale_configuration': {'key': 'properties.autoScaleConfiguration', 'type': 'ExpressRouteGatewayPropertiesAutoScaleConfiguration'},
        'express_route_connections': {'key': 'properties.expressRouteConnections', 'type': '[ExpressRouteConnection]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'virtual_hub': {'key': 'properties.virtualHub', 'type': 'VirtualHubId'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExpressRouteGateway, self).__init__(**kwargs)
        self.auto_scale_configuration = kwargs.get('auto_scale_configuration', None)
        self.express_route_connections = None
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.virtual_hub = kwargs.get('virtual_hub', None)
        self.etag = None
