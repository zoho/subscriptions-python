import json
import logging
import sys

import jsons as jsons
import requests
from urllib.parse import urlencode
from subscriptions.net import Util
from subscriptions.net.GenericListParams import GenericListParams
from subscriptions.net.ZSClient import ZSClient

_logger = logging.getLogger(__name__)


class RequestUtil:

    @staticmethod
    def execute( method, path, classobj=None, params=GenericListParams()):
        url = "%s/%s" % (ZSClient.get_Base_url(), path)
        headers = dict()
        try:
            querStr = RequestUtil.constructQuery(classobj, params)
            if method.lower() in ('get', 'delete'):
                url = '%s?%s' % (url, querStr)
                payload = None
            else:
                payload = querStr
                headers['Content-type'] = 'application/json'
            return RequestUtil.connection(method, url, payload, headers)
        except Exception as error:
            _logger.critical("Unable to connect to " + url + " due to " + str(error))
            raise sys.exit()

    @staticmethod
    def connection(method, url, payload, headers):
        headers.update({
            'User-Agent': ZSClient.get_user_agent_name(),
            'Accept': 'application/json',
            'Authorization': "Zoho-oauthtoken " + ZSClient.get_oauthtoken(),
            'Accept-Charset': ZSClient.CHARSET,
            'X-com-zoho-subscriptions-organizationid': ZSClient.get_organization_id()
        })
        try:
            response = requests.request(method, url, headers=headers, data=payload, timeout=30)
            return RequestUtil.handle_api_resp_error(url,response.status_code,response.json())
        except Exception as error:
            _logger.critical("Connection error:" + str(error))

    @staticmethod
    def constructQuery(classObj, params):
        query_parameter = ""
        if classObj is not None:
            return jsons.dumps(classObj)
        if params is not None:
            query = Util.serialize(params.get_query_params())
            query_parameter = urlencode(query)
        return query_parameter

    @staticmethod
    def handle_api_resp_error(url, http_code, resp_json):
        if http_code == 401:
            raise Exception("Authentication Exception\n Content:"+resp_json['message'])
        elif http_code >= 500:
            raise Exception("Server Error\n Content:"+resp_json['message'])
        elif 200 <= http_code <= 299:
            return json.dumps(resp_json, indent=2)
        else:
            raise Exception(resp_json['message'])


