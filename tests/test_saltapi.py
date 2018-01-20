import unittest
from buttersalt_saltapi import saltapi
from config import config


salt = saltapi.SaltApi(baseurl=config['testing'].SALT_API,
                       username=config['testing'].SALT_USERNAME,
                       password=config['testing'].SALT_PASSWORD)


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

