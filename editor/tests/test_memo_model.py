from django.test import TestCase

from editor.models import Memo


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
