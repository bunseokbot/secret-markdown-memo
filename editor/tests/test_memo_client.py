from django.test import Client, TestCase


class MemoClientTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_show_all_memo(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_new_memo(self):
        response = self.client.post('/editor/', {'title': 'test', 'content': '#test'})
        self.assertEqual(response.status_code, 302)

    def test_access_invalid_memo(self):
        response = self.client.get('/editor/1/')
        self.assertEqual(response.status_code, 404)
