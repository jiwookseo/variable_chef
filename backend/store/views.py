from django.shortcuts import render
from rest_framework import generics
from .serializers import VariableSerializer
from .models import Word, Variable


class ListVar(generics.ListCreateAPIView):
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer


class DetailVar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer


def index(request):
    word = request.GET.get('word', None)
    if word:
        temp = Word.objects.filter(kr_word=word)
        word = temp[0] if temp else Word.create(word)
        # session 당 1번 제한, 모든 Variables 조회 수 증가
        # if not request.session.get(str(word.id) + 'hit', False):
        #     request.session[str(word.id) + 'hit'] = True
        #     for var in word.variable_set.all():
        #         var.update_hits
    return render(request, 'store/index.html', {'word': word})
