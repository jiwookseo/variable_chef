from django.db import models
from . import recipe


class Recipe(models.Model):
    name = models.CharField(max_length=50, unique=True)
    wrong = models.CharField(max_length=50, default=None, blank=True, null=True)
    short = models.CharField(max_length=50, default=None, blank=True, null=True)
    slice = models.CharField(max_length=50, default=None, blank=True, null=True)
    sound = models.CharField(max_length=50, default=None, blank=True, null=True)

    @classmethod
    def create(cls, name, wrong=None, short=None):
        if cls.objects.filter(name=name):
            return None
        res = cls(name=name, wrong=wrong, short=short, slice=name[:3], sound=recipe.consonant(name))
        res.save()
        return res
