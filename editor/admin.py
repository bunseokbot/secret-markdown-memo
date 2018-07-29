from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Memo


admin.site.register(Memo, MarkdownxModelAdmin)
