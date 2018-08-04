from django import forms

from markdownx.fields import MarkdownxFormField

from editor.models import Memo


class MemoForm(forms.ModelForm):
    content = MarkdownxFormField()

    class Meta:
        model = Memo
        fields = ('title', 'content', )
