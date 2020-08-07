import unittest
import get_visitors
from unittest import mock
import os

@mock.patch.dict(os.environ, {"dbName": "sbargery_visitor_count"})

class TestGet_Visitors(unittest.TestCase):

    def test_status_output(self):
        event = []
        context = []
        output = get_visitors.lambda_handler(event, context)
        test_result = (output['statusCode'] == 200)
        self.assertTrue(test_result)

    def test_count_output(self):
        event = []
        context = []
        output = get_visitors.lambda_handler(event, context)
        test_result = isinstance(output['body'], int)
        self.assertTrue(test_result)

if (__name__ == '__main__'):
    unittest.main()