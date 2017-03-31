# coding: utf-8
from requests_mock import mock
from push7 import Client
from push7.push import PushWithQuery as query
import unittest


class APITest(unittest.TestCase):
    def setUp(self):
        appno, apikey = 'hoge', 'hoge'
        self.client = Client(appno, apikey)

    def test_push(self):
        self.client.push("poe", "poe", "http://google.com",
                         "http://google.com").send()

    def test_push_with_query(self):
        parameters = ['user001']
        self.client.push_with_query("poe", "poe", "http://google.com",
                                    "http://google.com", query.Mode._or,
                                    parameters).send()
