import unittest
from mock import Mock, call
from nose.tools import eq_
from wepay import WePay


class TestAPI(unittest.TestCase):

    def setUp(self):
        pass

    def test_default_timeout_is_passed_to_requests(self):
        api = WePay()
        api.requests = Mock()
        api.call('/some_uri')
        eq_([call('https://wepayapi.com/v2/some_uri',
                  headers={'Content-Type': 'application/json',
                           'User-Agent': 'WePay Python SDK'},
                  data=None, timeout=30)],
            api.requests.post.call_args_list)

    def test_customized_timeout_is_passed_to_requests(self):
        api = WePay(request_timeout=45)
        api.requests = Mock()
        api.call('/some_uri')
        eq_([call('https://wepayapi.com/v2/some_uri',
                  headers={'Content-Type': 'application/json',
                           'User-Agent': 'WePay Python SDK'},
                  data=None, timeout=45)],
            api.requests.post.call_args_list)

if __name__ == '__main__':
    unittest.main()