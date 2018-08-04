from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from editor.forms import MemoForm
from editor.models import Memo


def all_memo(request):
    query = request.GET.get('query', None)

    memos = Memo.objects.order_by('-idx')

    if query:
        memos = memos.filter(title__contains=query)
    else:
        memos = memos.all()

    return render(request, 'editor/all.html', {'memos': memos})


class Editor(View):
    def get(self, request, memo_id=None):
        if memo_id:
            # view specific memo
            memo = get_object_or_404(Memo, pk=memo_id)
            return render(request, 'editor/edit.html', {
                'form': MemoForm(instance=memo)
            })

        else:
            # add new memo mode
            return render(request, 'editor/new.html', {'form': MemoForm})

    def post(self, request, memo_id=None):
        form = MemoForm(request.POST)

        if memo_id:
            memo = get_object_or_404(Memo, pk=memo_id)
            form = MemoForm(request.POST, instance=memo)

        form.save()

        return redirect('/')
