from django.shortcuts import render

from editor.forms import MemoForm


def index(request):
    return render(request, 'editor/index.html', {'form': MemoForm})
