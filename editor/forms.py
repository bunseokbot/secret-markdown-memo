from django import forms

from markdownx.fields import MarkdownxFormField


class MemoForm(forms.Form):
    memo = MarkdownxFormField()
