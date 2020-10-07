# coding: utf-8

"""
    Qarax API

    The API for Qarax manager  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import qarax
from qarax.models.kernel import Kernel  # noqa: E501
from qarax.rest import ApiException

class TestKernel(unittest.TestCase):
    """Kernel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Kernel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = qarax.models.kernel.Kernel()  # noqa: E501
        if include_optional :
            return Kernel(
                id = '0', 
                name = '0', 
                storage_id = '0'
            )
        else :
            return Kernel(
        )

    def testKernel(self):
        """Test Kernel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
