from django.db import models
from cook import recipe


class Word(models.Model):
    kr_word = models.CharField(max_length=100, unique=True)
    en_word = models.CharField(max_length=200, blank=True, null=True)

    @classmethod
    def create(cls, kr_word):
        ok, en_word, filtered_words = recipe.cook(kr_word)
        if not ok:
            print('Fail to translate word')
            return None
        res = cls(kr_word=kr_word, en_word=en_word)
        res.save()
        print('Create Word object')
        Variable.create(en_word, res)
        for filtered in filtered_words:
            if en_word != filtered:
                Variable.create(filtered, res)
        print('Create Variable objects')
        return res

    def __str__(self):
        return f"{self.kr_word} : {self.en_word}"

    def __repr__(self):
        return f"{self.kr_word} : {self.en_word}"


class Variable(models.Model):
    name = models.CharField(max_length=200)  # lowercase split by space
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    @classmethod
    def create(cls, name, word):
        if cls.objects.filter(name=name):
            return None
        res = cls(name=name, word=word)
        res.save()
        snake = name.replace(' ', '_')
        Case.create(name=snake, variable=res, type='snake')
        pascal = name.title().replace(' ', '')
        Case.create(name=pascal, variable=res, type='pascal')
        camel = pascal[0].lower() + pascal[1:]
        Case.create(name=camel, variable=res, type='camel')
        return res

    def __str__(self):
        return f"{self.word.kr_word} > {self.name}"

    def __repr__(self):
        return f"{self.word.kr_word} > {self.name}"


class Case(models.Model):
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    hits = models.IntegerField(default=0)

    @classmethod
    def create(cls, name, variable, type):
        res = cls(name=name, variable=variable, type=type)
        res.save()
        return res

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
