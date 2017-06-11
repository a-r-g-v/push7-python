# coding: utf-8
from requests_mock import mock
from push7 import Client
from push7.push import PushWithQuery as query
import unittest
import os


class APITest(unittest.TestCase):
    def setUp(self):
        self.appno = os.environ.get('PUSH7_APPNO')
        self.apikey = os.environ.get('PUSH7_APIKEY')

        if not self.appno or not self.apikey:
            raise unittest.SkipTest

        self.client = Client(self.appno, self.apikey)

    def test_push(self):
        self.client.push("poe", "poe", "http://google.com",
                         "http://google.com").send()

    def test_push_with_query(self):
        parameters = ['user001']
        self.client.push_with_query("poe", "poe", "http://google.com",
                                    "http://google.com", query.Mode._or,
                                    parameters).send()
