import unittest
import create_visitor
import boto3
from unittest import mock
import os

# set the table name environment variable
@mock.patch.dict(os.environ, {"dbName_visitors": "sbargery_visitors", "dbName": "sbargery_visitor_count"})

class TestCreate_Visitor(unittest.TestCase):

    def test_db_connection(self):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('sbargery_visitors')
        self.assertEqual(table, dynamodb.Table(name='sbargery_visitors'))

    def test_status_output(self):
        event = {'sourceIP':'127.0.0.1'}
        context = []
        output = create_visitor.lambda_handler(event, context)
        test_result = (output['statusCode'] == 200)
        self.assertTrue(test_result)

if (__name__ == '__main__'):
    unittest.main()