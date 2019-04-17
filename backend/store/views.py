from django.shortcuts import render
from rest_framework import generics
from .serializers import VariableSerializer, WordSerializer
from .models import Word, Variable


class ListWord(generics.ListCreateAPIView):
    serializer_class = WordSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Word.objects.all()
        q = self.request.query_params.get('q', None)
        if q:
            queryset = queryset.filter(kr_word=q)
        return queryset


class DetailWord(generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class ListVar(generics.ListCreateAPIView):
    serializer_class = VariableSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Variable.objects.all()
        word = self.request.query_params.get('word', None)
        if word:
            queryset = queryset.filter(word=word)
        return queryset


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
