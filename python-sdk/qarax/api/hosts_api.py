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


class HostsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def hosts_get(self, **kwargs):  # noqa: E501
        """Get hosts list  # noqa: E501

        Get hosts list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hosts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Host]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.hosts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.hosts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def hosts_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get hosts list  # noqa: E501

        Get hosts list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hosts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Host]
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
                    " to method hosts_get" % key
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
            '/hosts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Host]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def hosts_host_id_get(self, host_id, **kwargs):  # noqa: E501
        """Get host by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hosts_host_id_get(host_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str host_id: ID of host (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.hosts_host_id_get_with_http_info(host_id, **kwargs)  # noqa: E501
        else:
            (data) = self.hosts_host_id_get_with_http_info(host_id, **kwargs)  # noqa: E501
            return data

    def hosts_host_id_get_with_http_info(self, host_id, **kwargs):  # noqa: E501
        """Get host by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hosts_host_id_get_with_http_info(host_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str host_id: ID of host (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['host_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hosts_host_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'host_id' is set
        if ('host_id' not in params or
                params['host_id'] is None):
            raise ValueError("Missing the required parameter `host_id` when calling `hosts_host_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'host_id' in params:
            path_params['hostId'] = params['host_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/hosts/{hostId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def hosts_host_id_health_get(self, host_id, **kwargs):  # noqa: E501
        """Host health check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hosts_host_id_health_get(host_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str host_id: ID of host (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.hosts_host_id_health_get_with_http_info(host_id, **kwargs)  # noqa: E501
        else:
            (data) = self.hosts_host_id_health_get_with_http_info(host_id, **kwargs)  # noqa: E501
            return data

    def hosts_host_id_health_get_with_http_info(self, host_id, **kwargs):  # noqa: E501
        """Host health check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hosts_host_id_health_get_with_http_info(host_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str host_id: ID of host (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['host_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hosts_host_id_health_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'host_id' is set
        if ('host_id' not in params or
                params['host_id'] is None):
            raise ValueError("Missing the required parameter `host_id` when calling `hosts_host_id_health_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'host_id' in params:
            path_params['hostId'] = params['host_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/hosts/{hostId}/health', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def hosts_host_id_install_post(self, host_id, **kwargs):  # noqa: E501
        """Install qarax node on host  # noqa: E501

        Install and run qarax-node on host  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hosts_host_id_install_post(host_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str host_id: ID of host (required)
        :param InstallHost body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.hosts_host_id_install_post_with_http_info(host_id, **kwargs)  # noqa: E501
        else:
            (data) = self.hosts_host_id_install_post_with_http_info(host_id, **kwargs)  # noqa: E501
            return data

    def hosts_host_id_install_post_with_http_info(self, host_id, **kwargs):  # noqa: E501
        """Install qarax node on host  # noqa: E501

        Install and run qarax-node on host  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hosts_host_id_install_post_with_http_info(host_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str host_id: ID of host (required)
        :param InstallHost body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['host_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hosts_host_id_install_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'host_id' is set
        if ('host_id' not in params or
                params['host_id'] is None):
            raise ValueError("Missing the required parameter `host_id` when calling `hosts_host_id_install_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'host_id' in params:
            path_params['hostId'] = params['host_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/hosts/{hostId}/install', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def hosts_post(self, body, **kwargs):  # noqa: E501
        """Create new host  # noqa: E501

        Create new host  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hosts_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Host body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.hosts_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.hosts_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def hosts_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create new host  # noqa: E501

        Create new host  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hosts_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Host body: (required)
        :return: None
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
                    " to method hosts_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `hosts_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/hosts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)