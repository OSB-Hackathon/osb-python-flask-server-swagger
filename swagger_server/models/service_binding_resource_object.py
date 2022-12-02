# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ServiceBindingResourceObject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, app_guid: str=None, route: str=None):  # noqa: E501
        """ServiceBindingResourceObject - a model defined in Swagger

        :param app_guid: The app_guid of this ServiceBindingResourceObject.  # noqa: E501
        :type app_guid: str
        :param route: The route of this ServiceBindingResourceObject.  # noqa: E501
        :type route: str
        """
        self.swagger_types = {
            'app_guid': str,
            'route': str
        }

        self.attribute_map = {
            'app_guid': 'app_guid',
            'route': 'route'
        }

        self._app_guid = app_guid
        self._route = route

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceBindingResourceObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceBindingResourceObject of this ServiceBindingResourceObject.  # noqa: E501
        :rtype: ServiceBindingResourceObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_guid(self) -> str:
        """Gets the app_guid of this ServiceBindingResourceObject.


        :return: The app_guid of this ServiceBindingResourceObject.
        :rtype: str
        """
        return self._app_guid

    @app_guid.setter
    def app_guid(self, app_guid: str):
        """Sets the app_guid of this ServiceBindingResourceObject.


        :param app_guid: The app_guid of this ServiceBindingResourceObject.
        :type app_guid: str
        """

        self._app_guid = app_guid

    @property
    def route(self) -> str:
        """Gets the route of this ServiceBindingResourceObject.


        :return: The route of this ServiceBindingResourceObject.
        :rtype: str
        """
        return self._route

    @route.setter
    def route(self, route: str):
        """Sets the route of this ServiceBindingResourceObject.


        :param route: The route of this ServiceBindingResourceObject.
        :type route: str
        """

        self._route = route
