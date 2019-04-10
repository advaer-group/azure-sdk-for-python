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

from .linked_service import LinkedService


class SquareLinkedService(LinkedService):
    """Square Service linked service.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param host: Required. The URL of the Square instance. (i.e.
     mystore.mysquare.com)
    :type host: object
    :param client_id: Required. The client ID associated with your Square
     application.
    :type client_id: object
    :param client_secret: The client secret associated with your Square
     application.
    :type client_secret: ~azure.mgmt.datafactory.models.SecretBase
    :param redirect_uri: Required. The redirect URL assigned in the Square
     application dashboard. (i.e. http://localhost:2500)
    :type redirect_uri: object
    :param use_encrypted_endpoints: Specifies whether the data source
     endpoints are encrypted using HTTPS. The default value is true.
    :type use_encrypted_endpoints: object
    :param use_host_verification: Specifies whether to require the host name
     in the server's certificate to match the host name of the server when
     connecting over SSL. The default value is true.
    :type use_host_verification: object
    :param use_peer_verification: Specifies whether to verify the identity of
     the server when connecting over SSL. The default value is true.
    :type use_peer_verification: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'host': {'required': True},
        'client_id': {'required': True},
        'redirect_uri': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'host': {'key': 'typeProperties.host', 'type': 'object'},
        'client_id': {'key': 'typeProperties.clientId', 'type': 'object'},
        'client_secret': {'key': 'typeProperties.clientSecret', 'type': 'SecretBase'},
        'redirect_uri': {'key': 'typeProperties.redirectUri', 'type': 'object'},
        'use_encrypted_endpoints': {'key': 'typeProperties.useEncryptedEndpoints', 'type': 'object'},
        'use_host_verification': {'key': 'typeProperties.useHostVerification', 'type': 'object'},
        'use_peer_verification': {'key': 'typeProperties.usePeerVerification', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(SquareLinkedService, self).__init__(**kwargs)
        self.host = kwargs.get('host', None)
        self.client_id = kwargs.get('client_id', None)
        self.client_secret = kwargs.get('client_secret', None)
        self.redirect_uri = kwargs.get('redirect_uri', None)
        self.use_encrypted_endpoints = kwargs.get('use_encrypted_endpoints', None)
        self.use_host_verification = kwargs.get('use_host_verification', None)
        self.use_peer_verification = kwargs.get('use_peer_verification', None)
        self.encrypted_credential = kwargs.get('encrypted_credential', None)
        self.type = 'Square'
