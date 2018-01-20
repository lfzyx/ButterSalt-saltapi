import unittest
import os
from buttersalt_saltapi import saltapi


salt = saltapi.SaltApi(baseurl=os.environ.get('SALT_API') or "http://127.0.0.1:8000",
                       username=os.environ.get('SALT_USERNAME') or "buttersalt",
                       password=os.environ.get('SALT_PASSWORD') or "buttersalt")


class ServerTestCase(unittest.TestCase):

    def test_login(self):
        re = salt.login()
        self.assertTrue(re)

    def test_get_keys(self):
        re = salt.get_keys()
        self.assertIsInstance(re.get('minions'), list)

    def test_get_jobs(self):
        re = salt.get_jobs()
        self.assertIsInstance(re, dict)

    def test_get_minions(self):
        re = salt.get_minions()
        self.assertIsInstance(re, dict)

    def test_get_stats(self):
        re = salt.get_stats()
        self.assertIsInstance(re, dict)

