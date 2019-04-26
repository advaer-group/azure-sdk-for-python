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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class SmartGroupsOperations(object):
    """SmartGroupsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: client API version. Possible values include: '2019-05-05-preview', '2018-05-05'. Constant value: "2019-05-05-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-05-05-preview"

        self.config = config

    def get_all(
            self, target_resource=None, target_resource_group=None, target_resource_type=None, monitor_service=None, monitor_condition=None, severity=None, smart_group_state=None, time_range=None, page_count=None, sort_by=None, sort_order=None, custom_headers=None, raw=False, **operation_config):
        """Get all smartGroups within the subscription.

        List all the smartGroups within the specified subscription. .

        :param target_resource: filter by target resource
        :type target_resource: str
        :param target_resource_group: filter by target resource group name
        :type target_resource_group: str
        :param target_resource_type: filter by target resource type
        :type target_resource_type: str
        :param monitor_service: filter by monitor service which is the source
         of the alert object. Possible values include: 'Platform', 'Application
         Insights', 'Log Analytics', 'Infrastructure Insights', 'ActivityLog
         Administrative', 'ActivityLog Security', 'ActivityLog Recommendation',
         'ActivityLog Policy', 'ActivityLog Autoscale', 'ServiceHealth',
         'SmartDetector', 'Zabbix', 'SCOM', 'Nagios'
        :type monitor_service: str or
         ~azure.mgmt.alertsmanagement.models.MonitorService
        :param monitor_condition: filter by monitor condition which is the
         state of the alert at monitor service. Possible values include:
         'Fired', 'Resolved'
        :type monitor_condition: str or
         ~azure.mgmt.alertsmanagement.models.MonitorCondition
        :param severity: filter by severity. Possible values include: 'Sev0',
         'Sev1', 'Sev2', 'Sev3', 'Sev4'
        :type severity: str or ~azure.mgmt.alertsmanagement.models.Severity
        :param smart_group_state: filter by state. Possible values include:
         'New', 'Acknowledged', 'Closed'
        :type smart_group_state: str or
         ~azure.mgmt.alertsmanagement.models.AlertState
        :param time_range: filter by time range, default value is 1 day.
         Possible values include: '1h', '1d', '7d', '30d'
        :type time_range: str or ~azure.mgmt.alertsmanagement.models.TimeRange
        :param page_count: number of items per page, default value is '25'.
        :type page_count: int
        :param sort_by: sort the query results by input field, default value
         is 'lastModifiedDateTime'. Possible values include: 'alertsCount',
         'state', 'severity', 'startDateTime', 'lastModifiedDateTime'
        :type sort_by: str or
         ~azure.mgmt.alertsmanagement.models.SmartGroupsSortByFields
        :param sort_order: sort the query results order in either ascending or
         descending, default value is 'desc' for time fields and 'asc' for
         others. Possible values include: 'asc', 'desc'
        :type sort_order: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SmartGroupsList or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.alertsmanagement.models.SmartGroupsList or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.alertsmanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_all.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if target_resource is not None:
            query_parameters['targetResource'] = self._serialize.query("target_resource", target_resource, 'str')
        if target_resource_group is not None:
            query_parameters['targetResourceGroup'] = self._serialize.query("target_resource_group", target_resource_group, 'str')
        if target_resource_type is not None:
            query_parameters['targetResourceType'] = self._serialize.query("target_resource_type", target_resource_type, 'str')
        if monitor_service is not None:
            query_parameters['monitorService'] = self._serialize.query("monitor_service", monitor_service, 'str')
        if monitor_condition is not None:
            query_parameters['monitorCondition'] = self._serialize.query("monitor_condition", monitor_condition, 'str')
        if severity is not None:
            query_parameters['severity'] = self._serialize.query("severity", severity, 'str')
        if smart_group_state is not None:
            query_parameters['smartGroupState'] = self._serialize.query("smart_group_state", smart_group_state, 'str')
        if time_range is not None:
            query_parameters['timeRange'] = self._serialize.query("time_range", time_range, 'str')
        if page_count is not None:
            query_parameters['pageCount'] = self._serialize.query("page_count", page_count, 'int')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, 'str')
        if sort_order is not None:
            query_parameters['sortOrder'] = self._serialize.query("sort_order", sort_order, 'str')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SmartGroupsList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_all.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups'}

    def get_by_id(
            self, smart_group_id, custom_headers=None, raw=False, **operation_config):
        """Get information of smart alerts group.

        Get details of smart group.

        :param smart_group_id: Smart Group Id
        :type smart_group_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SmartGroup or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.alertsmanagement.models.SmartGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.alertsmanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_by_id.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'smartGroupId': self._serialize.url("smart_group_id", smart_group_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('SmartGroup', response)
            header_dict = {
                'x-ms-request-id': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get_by_id.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}'}

    def change_state(
            self, smart_group_id, new_state, custom_headers=None, raw=False, **operation_config):
        """Change the state from unresolved to resolved and all the alerts within
        the smart group will also be resolved.

        :param smart_group_id: Smart Group Id
        :type smart_group_id: str
        :param new_state: filter by state. Possible values include: 'New',
         'Acknowledged', 'Closed'
        :type new_state: str or ~azure.mgmt.alertsmanagement.models.AlertState
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SmartGroup or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.alertsmanagement.models.SmartGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.alertsmanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.change_state.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'smartGroupId': self._serialize.url("smart_group_id", smart_group_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        query_parameters['newState'] = self._serialize.query("new_state", new_state, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('SmartGroup', response)
            header_dict = {
                'x-ms-request-id': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    change_state.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/changeState'}

    def get_history(
            self, smart_group_id, custom_headers=None, raw=False, **operation_config):
        """Get the history of the changes of smart group.

        :param smart_group_id: Smart Group Id
        :type smart_group_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SmartGroupModification or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.alertsmanagement.models.SmartGroupModification or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.alertsmanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_history.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'smartGroupId': self._serialize.url("smart_group_id", smart_group_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SmartGroupModification', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_history.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/history'}
