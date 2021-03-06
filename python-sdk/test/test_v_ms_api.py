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
from qarax.api.v_ms_api import VMsApi  # noqa: E501
from qarax.rest import ApiException


class TestVMsApi(unittest.TestCase):
    """VMsApi unit test stubs"""

    def setUp(self):
        self.api = VMsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_vms_get(self):
        """Test case for vms_get

        get vms list  # noqa: E501
        """
        pass

    def test_vms_post(self):
        """Test case for vms_post

        Add new VM  # noqa: E501
        """
        pass

    def test_vms_vm_id_drives_drive_id_attach_post(self):
        """Test case for vms_vm_id_drives_drive_id_attach_post

        Add drive to VM  # noqa: E501
        """
        pass

    def test_vms_vm_id_drives_get(self):
        """Test case for vms_vm_id_drives_get

        """
        pass

    def test_vms_vm_id_get(self):
        """Test case for vms_vm_id_get

        VM details  # noqa: E501
        """
        pass

    def test_vms_vm_id_start_post(self):
        """Test case for vms_vm_id_start_post

        Start VM  # noqa: E501
        """
        pass

    def test_vms_vm_id_stop_post(self):
        """Test case for vms_vm_id_stop_post

        Stop VM  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
