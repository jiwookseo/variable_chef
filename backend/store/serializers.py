from rest_framework import serializers
from .models import Variable


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
