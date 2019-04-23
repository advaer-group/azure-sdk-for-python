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


class ApplicationGatewayRewriteRule(Model):
    """Rewrite rule of an application gateway.

    :param name: Name of the rewrite rule that is unique within an Application
     Gateway.
    :type name: str
    :param rule_sequence: Rule Sequence of the rewrite rule that determines
     the order of execution of a particular rule in a RewriteRuleSet.
    :type rule_sequence: int
    :param conditions: Conditions based on which the action set execution will
     be evaluated.
    :type conditions:
     list[~azure.mgmt.network.v2019_02_01.models.ApplicationGatewayRewriteRuleCondition]
    :param action_set: Set of actions to be done as part of the rewrite Rule.
    :type action_set:
     ~azure.mgmt.network.v2019_02_01.models.ApplicationGatewayRewriteRuleActionSet
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'rule_sequence': {'key': 'ruleSequence', 'type': 'int'},
        'conditions': {'key': 'conditions', 'type': '[ApplicationGatewayRewriteRuleCondition]'},
        'action_set': {'key': 'actionSet', 'type': 'ApplicationGatewayRewriteRuleActionSet'},
    }

    def __init__(self, *, name: str=None, rule_sequence: int=None, conditions=None, action_set=None, **kwargs) -> None:
        super(ApplicationGatewayRewriteRule, self).__init__(**kwargs)
        self.name = name
        self.rule_sequence = rule_sequence
        self.conditions = conditions
        self.action_set = action_set
