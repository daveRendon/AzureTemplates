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


class ServiceBusMessage(Model):
    """ServiceBusMessage.

    :param authentication: Gets or sets the authentication.
    :type authentication: :class:`ServiceBusAuthentication
     <azure.mgmt.scheduler.models.ServiceBusAuthentication>`
    :param brokered_message_properties: Gets or sets the brokered message
     properties.
    :type brokered_message_properties:
     :class:`ServiceBusBrokeredMessageProperties
     <azure.mgmt.scheduler.models.ServiceBusBrokeredMessageProperties>`
    :param custom_message_properties: Gets or sets the custom message
     properties.
    :type custom_message_properties: dict
    :param message: Gets or sets the message.
    :type message: str
    :param namespace: Gets or sets the namespace.
    :type namespace: str
    :param transport_type: Gets or sets the transport type. Possible values
     include: 'NotSpecified', 'NetMessaging', 'AMQP'
    :type transport_type: str or :class:`ServiceBusTransportType
     <azure.mgmt.scheduler.models.ServiceBusTransportType>`
    """ 

    _attribute_map = {
        'authentication': {'key': 'authentication', 'type': 'ServiceBusAuthentication'},
        'brokered_message_properties': {'key': 'brokeredMessageProperties', 'type': 'ServiceBusBrokeredMessageProperties'},
        'custom_message_properties': {'key': 'customMessageProperties', 'type': '{str}'},
        'message': {'key': 'message', 'type': 'str'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'transport_type': {'key': 'transportType', 'type': 'ServiceBusTransportType'},
    }

    def __init__(self, authentication=None, brokered_message_properties=None, custom_message_properties=None, message=None, namespace=None, transport_type=None):
        self.authentication = authentication
        self.brokered_message_properties = brokered_message_properties
        self.custom_message_properties = custom_message_properties
        self.message = message
        self.namespace = namespace
        self.transport_type = transport_type
