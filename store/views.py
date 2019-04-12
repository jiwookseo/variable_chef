from django.shortcuts import render
from .models import Word


def index(request):
    word = request.GET.get('word', None)
    var_set = None
    if word:
        temp = Word.objects.filter(kr_word=word)
        word = temp[0] if temp else Word.create(word)
        var_set = word.variable_set.all()
        # session 당 1번 제한, 모든 Variables 조회 수 증가
        # if not request.session.get(str(word.id) + 'hit', False):
        #     request.session[str(word.id) + 'hit'] = True
        #     for var in var_set:
        #         var.update_hits
    return render(request, 'store/index.html', {'var_set': var_set})
