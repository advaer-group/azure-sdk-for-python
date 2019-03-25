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


class RegistrationAssignmentProperties(Model):
    """Properties of a registration assignment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param registration_definition_id: Required. Fully qualified path of the
     registration definition.
    :type registration_definition_id: str
    :ivar provisioning_state: Current state of the registration assignment.
     Possible values include: 'NotSpecified', 'Accepted', 'Running', 'Ready',
     'Creating', 'Created', 'Deleting', 'Deleted', 'Canceled', 'Failed',
     'Succeeded', 'Updating'
    :vartype provisioning_state: str or
     ~azure.mgmt.managedservices.models.ProvisioningState
    :ivar registration_definition: Registration definition inside registration
     assignment.
    :vartype registration_definition:
     ~azure.mgmt.managedservices.models.RegistrationAssignmentPropertiesRegistrationDefinition
    """

    _validation = {
        'registration_definition_id': {'required': True},
        'provisioning_state': {'readonly': True},
        'registration_definition': {'readonly': True},
    }

    _attribute_map = {
        'registration_definition_id': {'key': 'registrationDefinitionId', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'ProvisioningState'},
        'registration_definition': {'key': 'registrationDefinition', 'type': 'RegistrationAssignmentPropertiesRegistrationDefinition'},
    }

    def __init__(self, *, registration_definition_id: str, **kwargs) -> None:
        super(RegistrationAssignmentProperties, self).__init__(**kwargs)
        self.registration_definition_id = registration_definition_id
        self.provisioning_state = None
        self.registration_definition = None
