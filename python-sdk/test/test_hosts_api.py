# coding: utf-8

"""
    Qarax API

    The API for Qarax manager  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import qarax
from qarax.api.hosts_api import HostsApi  # noqa: E501
from qarax.rest import ApiException


class TestHostsApi(unittest.TestCase):
    """HostsApi unit test stubs"""

    def setUp(self):
        self.api = HostsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_hosts_get(self):
        """Test case for hosts_get

        Get hosts list  # noqa: E501
        """
        pass

    def test_hosts_host_id_get(self):
        """Test case for hosts_host_id_get

        Get host by ID  # noqa: E501
        """
        pass

    def test_hosts_host_id_health_get(self):
        """Test case for hosts_host_id_health_get

        Host health check  # noqa: E501
        """
        pass

    def test_hosts_host_id_install_post(self):
        """Test case for hosts_host_id_install_post

        Install qarax node on host  # noqa: E501
        """
        pass

    def test_hosts_post(self):
        """Test case for hosts_post

        Create new host  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
