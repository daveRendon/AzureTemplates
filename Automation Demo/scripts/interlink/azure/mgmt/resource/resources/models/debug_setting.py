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


class DebugSetting(Model):
    """DebugSetting.

    :param detail_level: The debug detail level.
    :type detail_level: str
    """ 

    _attribute_map = {
        'detail_level': {'key': 'detailLevel', 'type': 'str'},
    }

    def __init__(self, detail_level=None):
        self.detail_level = detail_level
