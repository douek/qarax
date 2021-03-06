# coding: utf-8

"""
    Qarax API

    The API for Qarax manager  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from qarax.api_client import ApiClient


class VMsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def vms_get(self, **kwargs):  # noqa: E501
        """get vms list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Vm]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vms_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.vms_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def vms_get_with_http_info(self, **kwargs):  # noqa: E501
        """get vms list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Vm]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vms_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vms/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Vm]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vms_post(self, **kwargs):  # noqa: E501
        """Add new VM  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Vm body:
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vms_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.vms_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def vms_post_with_http_info(self, **kwargs):  # noqa: E501
        """Add new VM  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Vm body:
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vms_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vms/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vms_vm_id_drives_drive_id_attach_post(self, vm_id, drive_id, **kwargs):  # noqa: E501
        """Add drive to VM  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_vm_id_drives_drive_id_attach_post(vm_id, drive_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_id: ID of a VM (required)
        :param str drive_id: ID of a drive (required)
        :return: list[AttachDrive]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vms_vm_id_drives_drive_id_attach_post_with_http_info(vm_id, drive_id, **kwargs)  # noqa: E501
        else:
            (data) = self.vms_vm_id_drives_drive_id_attach_post_with_http_info(vm_id, drive_id, **kwargs)  # noqa: E501
            return data

    def vms_vm_id_drives_drive_id_attach_post_with_http_info(self, vm_id, drive_id, **kwargs):  # noqa: E501
        """Add drive to VM  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_vm_id_drives_drive_id_attach_post_with_http_info(vm_id, drive_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_id: ID of a VM (required)
        :param str drive_id: ID of a drive (required)
        :return: list[AttachDrive]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vm_id', 'drive_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vms_vm_id_drives_drive_id_attach_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vm_id' is set
        if ('vm_id' not in params or
                params['vm_id'] is None):
            raise ValueError("Missing the required parameter `vm_id` when calling `vms_vm_id_drives_drive_id_attach_post`")  # noqa: E501
        # verify the required parameter 'drive_id' is set
        if ('drive_id' not in params or
                params['drive_id'] is None):
            raise ValueError("Missing the required parameter `drive_id` when calling `vms_vm_id_drives_drive_id_attach_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vm_id' in params:
            path_params['vmId'] = params['vm_id']  # noqa: E501
        if 'drive_id' in params:
            path_params['driveId'] = params['drive_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vms/{vmId}/drives/{driveId}/attach', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AttachDrive]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vms_vm_id_drives_get(self, vm_id, **kwargs):  # noqa: E501
        """vms_vm_id_drives_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_vm_id_drives_get(vm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_id: ID of a VM (required)
        :return: list[Drive]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vms_vm_id_drives_get_with_http_info(vm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.vms_vm_id_drives_get_with_http_info(vm_id, **kwargs)  # noqa: E501
            return data

    def vms_vm_id_drives_get_with_http_info(self, vm_id, **kwargs):  # noqa: E501
        """vms_vm_id_drives_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_vm_id_drives_get_with_http_info(vm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_id: ID of a VM (required)
        :return: list[Drive]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vms_vm_id_drives_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vm_id' is set
        if ('vm_id' not in params or
                params['vm_id'] is None):
            raise ValueError("Missing the required parameter `vm_id` when calling `vms_vm_id_drives_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vm_id' in params:
            path_params['vmId'] = params['vm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vms/{vmId}/drives/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Drive]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vms_vm_id_get(self, vm_id, **kwargs):  # noqa: E501
        """VM details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_vm_id_get(vm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_id: ID of a VM (required)
        :return: Vm
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vms_vm_id_get_with_http_info(vm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.vms_vm_id_get_with_http_info(vm_id, **kwargs)  # noqa: E501
            return data

    def vms_vm_id_get_with_http_info(self, vm_id, **kwargs):  # noqa: E501
        """VM details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_vm_id_get_with_http_info(vm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_id: ID of a VM (required)
        :return: Vm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vms_vm_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vm_id' is set
        if ('vm_id' not in params or
                params['vm_id'] is None):
            raise ValueError("Missing the required parameter `vm_id` when calling `vms_vm_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vm_id' in params:
            path_params['vmId'] = params['vm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vms/{vmId}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Vm',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vms_vm_id_start_post(self, vm_id, **kwargs):  # noqa: E501
        """Start VM  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_vm_id_start_post(vm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_id: ID of a VM (required)
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vms_vm_id_start_post_with_http_info(vm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.vms_vm_id_start_post_with_http_info(vm_id, **kwargs)  # noqa: E501
            return data

    def vms_vm_id_start_post_with_http_info(self, vm_id, **kwargs):  # noqa: E501
        """Start VM  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_vm_id_start_post_with_http_info(vm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_id: ID of a VM (required)
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vms_vm_id_start_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vm_id' is set
        if ('vm_id' not in params or
                params['vm_id'] is None):
            raise ValueError("Missing the required parameter `vm_id` when calling `vms_vm_id_start_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vm_id' in params:
            path_params['vmId'] = params['vm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vms/{vmId}/start', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vms_vm_id_stop_post(self, vm_id, **kwargs):  # noqa: E501
        """Stop VM  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_vm_id_stop_post(vm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_id: ID of a VM (required)
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vms_vm_id_stop_post_with_http_info(vm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.vms_vm_id_stop_post_with_http_info(vm_id, **kwargs)  # noqa: E501
            return data

    def vms_vm_id_stop_post_with_http_info(self, vm_id, **kwargs):  # noqa: E501
        """Stop VM  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vms_vm_id_stop_post_with_http_info(vm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_id: ID of a VM (required)
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vms_vm_id_stop_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vm_id' is set
        if ('vm_id' not in params or
                params['vm_id'] is None):
            raise ValueError("Missing the required parameter `vm_id` when calling `vms_vm_id_stop_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vm_id' in params:
            path_params['vmId'] = params['vm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vms/{vmId}/stop', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
