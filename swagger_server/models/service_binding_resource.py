# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.service_binding_endpoint import ServiceBindingEndpoint
from swagger_server.models.service_binding_metadata import ServiceBindingMetadata
from swagger_server.models.service_binding_volume_mount import ServiceBindingVolumeMount
from swagger_server import util


class ServiceBindingResource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: ServiceBindingMetadata=None, credentials: object=None, syslog_drain_url: str=None, route_service_url: str=None, volume_mounts: List[ServiceBindingVolumeMount]=None, endpoints: List[ServiceBindingEndpoint]=None, parameters: object=None):  # noqa: E501
        """ServiceBindingResource - a model defined in Swagger

        :param metadata: The metadata of this ServiceBindingResource.  # noqa: E501
        :type metadata: ServiceBindingMetadata
        :param credentials: The credentials of this ServiceBindingResource.  # noqa: E501
        :type credentials: object
        :param syslog_drain_url: The syslog_drain_url of this ServiceBindingResource.  # noqa: E501
        :type syslog_drain_url: str
        :param route_service_url: The route_service_url of this ServiceBindingResource.  # noqa: E501
        :type route_service_url: str
        :param volume_mounts: The volume_mounts of this ServiceBindingResource.  # noqa: E501
        :type volume_mounts: List[ServiceBindingVolumeMount]
        :param endpoints: The endpoints of this ServiceBindingResource.  # noqa: E501
        :type endpoints: List[ServiceBindingEndpoint]
        :param parameters: The parameters of this ServiceBindingResource.  # noqa: E501
        :type parameters: object
        """
        self.swagger_types = {
            'metadata': ServiceBindingMetadata,
            'credentials': object,
            'syslog_drain_url': str,
            'route_service_url': str,
            'volume_mounts': List[ServiceBindingVolumeMount],
            'endpoints': List[ServiceBindingEndpoint],
            'parameters': object
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'credentials': 'credentials',
            'syslog_drain_url': 'syslog_drain_url',
            'route_service_url': 'route_service_url',
            'volume_mounts': 'volume_mounts',
            'endpoints': 'endpoints',
            'parameters': 'parameters'
        }

        self._metadata = metadata
        self._credentials = credentials
        self._syslog_drain_url = syslog_drain_url
        self._route_service_url = route_service_url
        self._volume_mounts = volume_mounts
        self._endpoints = endpoints
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceBindingResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceBindingResource of this ServiceBindingResource.  # noqa: E501
        :rtype: ServiceBindingResource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> ServiceBindingMetadata:
        """Gets the metadata of this ServiceBindingResource.


        :return: The metadata of this ServiceBindingResource.
        :rtype: ServiceBindingMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: ServiceBindingMetadata):
        """Sets the metadata of this ServiceBindingResource.


        :param metadata: The metadata of this ServiceBindingResource.
        :type metadata: ServiceBindingMetadata
        """

        self._metadata = metadata

    @property
    def credentials(self) -> object:
        """Gets the credentials of this ServiceBindingResource.


        :return: The credentials of this ServiceBindingResource.
        :rtype: object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials: object):
        """Sets the credentials of this ServiceBindingResource.


        :param credentials: The credentials of this ServiceBindingResource.
        :type credentials: object
        """

        self._credentials = credentials

    @property
    def syslog_drain_url(self) -> str:
        """Gets the syslog_drain_url of this ServiceBindingResource.


        :return: The syslog_drain_url of this ServiceBindingResource.
        :rtype: str
        """
        return self._syslog_drain_url

    @syslog_drain_url.setter
    def syslog_drain_url(self, syslog_drain_url: str):
        """Sets the syslog_drain_url of this ServiceBindingResource.


        :param syslog_drain_url: The syslog_drain_url of this ServiceBindingResource.
        :type syslog_drain_url: str
        """

        self._syslog_drain_url = syslog_drain_url

    @property
    def route_service_url(self) -> str:
        """Gets the route_service_url of this ServiceBindingResource.


        :return: The route_service_url of this ServiceBindingResource.
        :rtype: str
        """
        return self._route_service_url

    @route_service_url.setter
    def route_service_url(self, route_service_url: str):
        """Sets the route_service_url of this ServiceBindingResource.


        :param route_service_url: The route_service_url of this ServiceBindingResource.
        :type route_service_url: str
        """

        self._route_service_url = route_service_url

    @property
    def volume_mounts(self) -> List[ServiceBindingVolumeMount]:
        """Gets the volume_mounts of this ServiceBindingResource.


        :return: The volume_mounts of this ServiceBindingResource.
        :rtype: List[ServiceBindingVolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts: List[ServiceBindingVolumeMount]):
        """Sets the volume_mounts of this ServiceBindingResource.


        :param volume_mounts: The volume_mounts of this ServiceBindingResource.
        :type volume_mounts: List[ServiceBindingVolumeMount]
        """

        self._volume_mounts = volume_mounts

    @property
    def endpoints(self) -> List[ServiceBindingEndpoint]:
        """Gets the endpoints of this ServiceBindingResource.


        :return: The endpoints of this ServiceBindingResource.
        :rtype: List[ServiceBindingEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints: List[ServiceBindingEndpoint]):
        """Sets the endpoints of this ServiceBindingResource.


        :param endpoints: The endpoints of this ServiceBindingResource.
        :type endpoints: List[ServiceBindingEndpoint]
        """

        self._endpoints = endpoints

    @property
    def parameters(self) -> object:
        """Gets the parameters of this ServiceBindingResource.


        :return: The parameters of this ServiceBindingResource.
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: object):
        """Sets the parameters of this ServiceBindingResource.


        :param parameters: The parameters of this ServiceBindingResource.
        :type parameters: object
        """

        self._parameters = parameters
