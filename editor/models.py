from django.db import models

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Memo(models.Model):
    idx = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    upload_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    content = MarkdownxField()

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title
