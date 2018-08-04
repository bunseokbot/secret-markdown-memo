from django.test import TestCase, Client

from editor.models import Memo


class MemoClientTest(TestCase):
    """Memo client functional test."""

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


class MemoModelTests(TestCase):
    """Memo model testcases."""

    def setUp(self):
        self.memo = Memo(title='basic memo')
        self.memo.save()

    def test_add_new_memo(self):
        """Test add new memo to database."""
        memo = Memo(title='memo test', content='#test')
        memo.save()

        self.assertEqual(memo.title, 'memo test')
        self.assertEqual(memo.content, '#test')

    def test_edit_memo(self):
        self.assertEqual(self.memo.title, 'basic memo')

        self.memo.title = 'basic edit memo'
        self.memo.save()

        self.assertEqual(self.memo.title, 'basic edit memo')
