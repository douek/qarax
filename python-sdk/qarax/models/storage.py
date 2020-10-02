# coding: utf-8

"""
    Qarax API

    The API for Qarax manager  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Storage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'config': 'object',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'storage_type': 'str'
    }

    attribute_map = {
        'config': 'config',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'storage_type': 'storage_type'
    }

    def __init__(self, config=None, id=None, name=None, status=None, storage_type=None):  # noqa: E501
        """Storage - a model defined in Swagger"""  # noqa: E501
        self._config = None
        self._id = None
        self._name = None
        self._status = None
        self._storage_type = None
        self.discriminator = None
        if config is not None:
            self.config = config
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if storage_type is not None:
            self.storage_type = storage_type

    @property
    def config(self):
        """Gets the config of this Storage.  # noqa: E501


        :return: The config of this Storage.  # noqa: E501
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Storage.


        :param config: The config of this Storage.  # noqa: E501
        :type: object
        """

        self._config = config

    @property
    def id(self):
        """Gets the id of this Storage.  # noqa: E501


        :return: The id of this Storage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Storage.


        :param id: The id of this Storage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Storage.  # noqa: E501


        :return: The name of this Storage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Storage.


        :param name: The name of this Storage.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this Storage.  # noqa: E501


        :return: The status of this Storage.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Storage.


        :param status: The status of this Storage.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def storage_type(self):
        """Gets the storage_type of this Storage.  # noqa: E501


        :return: The storage_type of this Storage.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this Storage.


        :param storage_type: The storage_type of this Storage.  # noqa: E501
        :type: str
        """

        self._storage_type = storage_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Storage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Storage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other