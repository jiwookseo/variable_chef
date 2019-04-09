from django.db import models
<<<<<<< HEAD
# from . import papago
=======
from . import papago, recipe
>>>>>>> 6b69bb745bfc15caea2af75e32d6d9dc6c6d4d7c


class Word(models.Model):
    kr_word = models.CharField(max_length=100, unique=True)
    en_word = models.TextField()

<<<<<<< HEAD
    def translate(self):
        # self.en_word = papago.translate(self.kr_word)
        return
=======
    @classmethod
    def create(cls, kr_word):
        ok, translated = papago.translate(kr_word)
        if ok:
            en_word = translated
            res = cls(kr_word=kr_word, en_word=en_word)
            res.save()
            print('Create Word object')
            Variable.create(en_word, res)
            temp = recipe.rcp1(en_word)
            Variable.create(temp, res)
            Variable.create(recipe.rcp2(temp), res)
            print('Create Variable objects')
            return res
        print('Fail to translate word')
        return None
>>>>>>> 6b69bb745bfc15caea2af75e32d6d9dc6c6d4d7c

    def __str__(self):
        return f"{self.kr_word} : {self.en_word}"

    def __repr__(self):
        return f"{self.kr_word} : {self.en_word}"


class Variable(models.Model):
    name = models.TextField(unique=True)  # lowercase split by space
    snake_case = models.TextField()
    camel_case = models.TextField()
    pascal_case = models.TextField()
    copy_hits = models.IntegerField(default=0)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    @classmethod
    def create(cls, name, word):
        if cls.objects.filter(name=name):
            return None
        snake_case = name.replace(' ', '_')
        pascal_case = name.title().replace(' ', '')
        camel_case = pascal_case[0].lower() + pascal_case[1:]
        res = cls(name=name, snake_case=snake_case, pascal_case=pascal_case, camel_case=camel_case, word=word)
        res.save()
        return res

    def __str__(self):
        return f"{self.word.kr_word} > {self.name}"

    def __repr__(self):
        return f"{self.word.kr_word} > {self.name}"
