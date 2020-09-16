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
from qarax.api.drives_api import DrivesApi  # noqa: E501
from qarax.rest import ApiException


class TestDrivesApi(unittest.TestCase):
    """DrivesApi unit test stubs"""

    def setUp(self):
        self.api = DrivesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_drives_get(self):
        """Test case for drives_get

        Get drives list  # noqa: E501
        """
        pass

    def test_drives_post(self):
        """Test case for drives_post

        Add new drive  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
