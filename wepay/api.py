import json


class WePay(object):

    """
    A client for the WePay API.
    """

    def __init__(
            self, target_environment="Production", access_token=None, internal_calls=False,
            api_version=None, request_timeout=30,
            ):
        """
        :param bool production: When ``False``, the ``stage.wepay.com`` API
            server will be used instead of the default production.
        :param str access_token: The access token associated with your
            application.
        """
        import requests
        self.requests = requests
        self.access_token = access_token
        self.api_version = api_version
        self.request_timeout = request_timeout
        self.internal_calls = internal_calls

        endpoint = "v2"

        if internal_calls:
            endpoint = "internal"

        if target_environment.lower() == "production":
            self.api_endpoint = "https://wepayapi.com/" + endpoint
            self.browser_endpoint = "https://www.wepay.com/" + endpoint
        if target_environment.lower() == "stage":
            self.api_endpoint = "https://stage.wepayapi.com/" + endpoint
            self.browser_endpoint = "https://stage.wepay.com/" + endpoint
        if target_environment.lower() == "stage-internal":
            self.api_endpoint = "https://internal-stage.wepayapi.com/" + endpoint
            self.browser_endpoint = "https://www.internal-stage.wepay-inc.com/" + endpoint
        if target_environment.lower() == "vm":
            self.api_endpoint = "http://vm.wepay.com/" + endpoint
            self.browser_endpoint = "http://vm.wepay.com/" + endpoint

    def call(self, uri, params=None, token=None):
        """
        Calls wepay.com/v2/``uri`` with ``params`` and returns the JSON
        response as a python dict. The optional token parameter will override
        the instance's access_token if it is set.

        :param str uri: The URI on the API endpoint to call.
        :param dict params: The parameters to pass to the URI.
        :param str token: Optional override for this ``WePay`` object's access
            token.
        """

        headers = {'Content-Type': 'application/json',
                   'User-Agent': 'WePay Python SDK'}
        url = self.api_endpoint + uri

        if self.internal_calls:
            print("Invoking WePay Internal calls")
        else:
            if self.access_token or token:
                headers['Authorization'] = 'Bearer ' + \
                    (token if token else self.access_token)

            if self.api_version:
                headers['Api-Version'] = self.api_version

        if params:
            params = json.dumps(params)

        try:
            response = self.requests.post(
                url, data=params, headers=headers,
                timeout=self.request_timeout)
            return response.json()
        except:
            if 400 <= response.status_code <= 599:
                raise Exception('Unknown error. Please contact support@wepay.com')


