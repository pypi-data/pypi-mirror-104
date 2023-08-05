# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.2
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrintOrder(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'uuid': 'str',
        'build_uuid': 'str',
        'total_copies': 'int',
        'created_at': 'datetime',
        'print_order_number': 'str',
        'print_order_tags': 'dict(str, str)',
        'notes': 'str',
        'routed_to': 'dict(str, PrintOrderRoutedTo)'
    }

    attribute_map = {
        'uuid': 'uuid',
        'build_uuid': 'build_uuid',
        'total_copies': 'total_copies',
        'created_at': 'created_at',
        'print_order_number': 'print_order_number',
        'print_order_tags': 'print_order_tags',
        'notes': 'notes',
        'routed_to': 'routed_to'
    }

    def __init__(self, uuid=None, build_uuid=None, total_copies=1, created_at=None, print_order_number=None, print_order_tags=None, notes=None, routed_to=None, local_vars_configuration=None):  # noqa: E501
        """PrintOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._build_uuid = None
        self._total_copies = None
        self._created_at = None
        self._print_order_number = None
        self._print_order_tags = None
        self._notes = None
        self._routed_to = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if build_uuid is not None:
            self.build_uuid = build_uuid
        if total_copies is not None:
            self.total_copies = total_copies
        if created_at is not None:
            self.created_at = created_at
        if print_order_number is not None:
            self.print_order_number = print_order_number
        if print_order_tags is not None:
            self.print_order_tags = print_order_tags
        if notes is not None:
            self.notes = notes
        if routed_to is not None:
            self.routed_to = routed_to

    @property
    def uuid(self):
        """Gets the uuid of this PrintOrder.  # noqa: E501

        The uuid of the print order  # noqa: E501

        :return: The uuid of this PrintOrder.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PrintOrder.

        The uuid of the print order  # noqa: E501

        :param uuid: The uuid of this PrintOrder.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def build_uuid(self):
        """Gets the build_uuid of this PrintOrder.  # noqa: E501

        The uuid of the build to be queued  # noqa: E501

        :return: The build_uuid of this PrintOrder.  # noqa: E501
        :rtype: str
        """
        return self._build_uuid

    @build_uuid.setter
    def build_uuid(self, build_uuid):
        """Sets the build_uuid of this PrintOrder.

        The uuid of the build to be queued  # noqa: E501

        :param build_uuid: The build_uuid of this PrintOrder.  # noqa: E501
        :type: str
        """

        self._build_uuid = build_uuid

    @property
    def total_copies(self):
        """Gets the total_copies of this PrintOrder.  # noqa: E501

        The total number of copies to be printed  # noqa: E501

        :return: The total_copies of this PrintOrder.  # noqa: E501
        :rtype: int
        """
        return self._total_copies

    @total_copies.setter
    def total_copies(self, total_copies):
        """Sets the total_copies of this PrintOrder.

        The total number of copies to be printed  # noqa: E501

        :param total_copies: The total_copies of this PrintOrder.  # noqa: E501
        :type: int
        """

        self._total_copies = total_copies

    @property
    def created_at(self):
        """Gets the created_at of this PrintOrder.  # noqa: E501

        Time when print order was created  # noqa: E501

        :return: The created_at of this PrintOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PrintOrder.

        Time when print order was created  # noqa: E501

        :param created_at: The created_at of this PrintOrder.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def print_order_number(self):
        """Gets the print_order_number of this PrintOrder.  # noqa: E501

        Customer-provided print order number  # noqa: E501

        :return: The print_order_number of this PrintOrder.  # noqa: E501
        :rtype: str
        """
        return self._print_order_number

    @print_order_number.setter
    def print_order_number(self, print_order_number):
        """Sets the print_order_number of this PrintOrder.

        Customer-provided print order number  # noqa: E501

        :param print_order_number: The print_order_number of this PrintOrder.  # noqa: E501
        :type: str
        """

        self._print_order_number = print_order_number

    @property
    def print_order_tags(self):
        """Gets the print_order_tags of this PrintOrder.  # noqa: E501

        Key value pairs to be associated with print order  # noqa: E501

        :return: The print_order_tags of this PrintOrder.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._print_order_tags

    @print_order_tags.setter
    def print_order_tags(self, print_order_tags):
        """Sets the print_order_tags of this PrintOrder.

        Key value pairs to be associated with print order  # noqa: E501

        :param print_order_tags: The print_order_tags of this PrintOrder.  # noqa: E501
        :type: dict(str, str)
        """

        self._print_order_tags = print_order_tags

    @property
    def notes(self):
        """Gets the notes of this PrintOrder.  # noqa: E501

        Notes associated with  # noqa: E501

        :return: The notes of this PrintOrder.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PrintOrder.

        Notes associated with  # noqa: E501

        :param notes: The notes of this PrintOrder.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def routed_to(self):
        """Gets the routed_to of this PrintOrder.  # noqa: E501

        Printers that this print order was routed to, keyed off printer serial number  # noqa: E501

        :return: The routed_to of this PrintOrder.  # noqa: E501
        :rtype: dict(str, PrintOrderRoutedTo)
        """
        return self._routed_to

    @routed_to.setter
    def routed_to(self, routed_to):
        """Sets the routed_to of this PrintOrder.

        Printers that this print order was routed to, keyed off printer serial number  # noqa: E501

        :param routed_to: The routed_to of this PrintOrder.  # noqa: E501
        :type: dict(str, PrintOrderRoutedTo)
        """

        self._routed_to = routed_to

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PrintOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintOrder):
            return True

        return self.to_dict() != other.to_dict()
