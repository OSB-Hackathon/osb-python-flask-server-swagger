# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.service_instance_metadata import ServiceInstanceMetadata
from swagger_server import util


class ServiceInstanceAsyncOperation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, dashboard_url: str=None, operation: str=None, metadata: ServiceInstanceMetadata=None):  # noqa: E501
        """ServiceInstanceAsyncOperation - a model defined in Swagger

        :param dashboard_url: The dashboard_url of this ServiceInstanceAsyncOperation.  # noqa: E501
        :type dashboard_url: str
        :param operation: The operation of this ServiceInstanceAsyncOperation.  # noqa: E501
        :type operation: str
        :param metadata: The metadata of this ServiceInstanceAsyncOperation.  # noqa: E501
        :type metadata: ServiceInstanceMetadata
        """
        self.swagger_types = {
            'dashboard_url': str,
            'operation': str,
            'metadata': ServiceInstanceMetadata
        }

        self.attribute_map = {
            'dashboard_url': 'dashboard_url',
            'operation': 'operation',
            'metadata': 'metadata'
        }

        self._dashboard_url = dashboard_url
        self._operation = operation
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceInstanceAsyncOperation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceInstanceAsyncOperation of this ServiceInstanceAsyncOperation.  # noqa: E501
        :rtype: ServiceInstanceAsyncOperation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dashboard_url(self) -> str:
        """Gets the dashboard_url of this ServiceInstanceAsyncOperation.


        :return: The dashboard_url of this ServiceInstanceAsyncOperation.
        :rtype: str
        """
        return self._dashboard_url

    @dashboard_url.setter
    def dashboard_url(self, dashboard_url: str):
        """Sets the dashboard_url of this ServiceInstanceAsyncOperation.


        :param dashboard_url: The dashboard_url of this ServiceInstanceAsyncOperation.
        :type dashboard_url: str
        """

        self._dashboard_url = dashboard_url

    @property
    def operation(self) -> str:
        """Gets the operation of this ServiceInstanceAsyncOperation.


        :return: The operation of this ServiceInstanceAsyncOperation.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation: str):
        """Sets the operation of this ServiceInstanceAsyncOperation.


        :param operation: The operation of this ServiceInstanceAsyncOperation.
        :type operation: str
        """

        self._operation = operation

    @property
    def metadata(self) -> ServiceInstanceMetadata:
        """Gets the metadata of this ServiceInstanceAsyncOperation.


        :return: The metadata of this ServiceInstanceAsyncOperation.
        :rtype: ServiceInstanceMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: ServiceInstanceMetadata):
        """Sets the metadata of this ServiceInstanceAsyncOperation.


        :param metadata: The metadata of this ServiceInstanceAsyncOperation.
        :type metadata: ServiceInstanceMetadata
        """

        self._metadata = metadata
