from rest_framework import serializers
from .models import Variable, Word


class VariableSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'word',
            'camel',
            'snake',
            'pascal',
            'hits',
        )
        model = Variable


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'kr_word',
            'en_word',
        )
        model = Word
