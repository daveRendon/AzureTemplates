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


class ExportRDBParameters(Model):
    """Parameters for redis export operation.

    :param format: File format.
    :type format: str
    :param prefix: Prifix to use for exported files.
    :type prefix: str
    :param container: Container name to export to.
    :type container: str
    """ 

    _validation = {
        'prefix': {'required': True},
        'container': {'required': True},
    }

    _attribute_map = {
        'format': {'key': 'format', 'type': 'str'},
        'prefix': {'key': 'prefix', 'type': 'str'},
        'container': {'key': 'container', 'type': 'str'},
    }

    def __init__(self, prefix, container, format=None):
        self.format = format
        self.prefix = prefix
        self.container = container
