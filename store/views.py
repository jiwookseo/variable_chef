from django.shortcuts import render
from .models import Word


def index(request):
    word = request.GET.get('word', None)
    var_set = None
    if word:
        temp = Word.objects.filter(kr_word=word)
        word = temp[0] if temp else Word.create(word)
        var_set = word.variable_set.order_by('-hits')
    return render(request, 'store/index.html', {'var_set': var_set})
