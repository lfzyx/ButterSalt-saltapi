import requests
import unittest
from config import config

url = config['default'].SALT_API
username = config['default'].SALT_USERNAME
password = config['default'].SALT_PASSWORD
token = requests.Session()
eauth = 'pam'


class ServerTestCase(unittest.TestCase):

    def test_root(self):
        re = token.get(url + '/').json()
        self.assertEqual('Welcome', re.get('return'))

    def test_nologin(self):
        re = token.get(url + '/login').json()
        self.assertIsNone(re.get('status'))

    def test_login(self):
        re = token.post(url + '/login', json={
            'username': username,
            'password': password,
            'eauth': eauth,
        }).json()
        self.assertTrue(re.get('return')[0].get('token'))

    def test_hook(self):
        token.post(url + '/login', json={
            'username': username,
            'password': password,
            'eauth': eauth,
        }).json()
        self.assertIs(token.post(url + '/hook/').json().get('success'), True)

    def test_minion(self):
        token.post(url + '/login', json={
            'username': username,
            'password': password,
            'eauth': eauth,
        }).json()
        self.assertIsInstance(token.get(url + '/minions/').json().get('return')[0], dict)

    def test_job(self):
        token.post(url + '/login', json={
            'username': username,
            'password': password,
            'eauth': eauth,
        }).json()
        self.assertIsInstance(token.get(url + '/jobs/').json().get('return')[0], dict)

    def test_keys(self):
        token.post(url + '/login', json={
            'username': username,
            'password': password,
            'eauth': eauth,
        }).json()
        self.assertIsInstance(token.get(url + '/keys/').json().get('return'), dict)

    def test_manage_up(self):
        token.post(url + '/login', json={
            'username': username,
            'password': password,
            'eauth': eauth,
        }).json()

        self.assertIsInstance(token.post(url, json={
            "client": "runner",
            "fun": "manage.up"
        }).json().get('return'), list)
