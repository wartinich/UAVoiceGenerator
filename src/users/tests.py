from users.models import User
from django.test import TestCase


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'laqpzd@gmail.com',
            'username': 'test',
            'password': 'secret'
        }
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code == 200)
