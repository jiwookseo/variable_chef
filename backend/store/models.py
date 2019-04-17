from django.db import models
from cook import recipe
from django.conf import settings


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
    snake = models.CharField(max_length=200, default='')
    pascal = models.CharField(max_length=200, default='')
    camel = models.CharField(max_length=200, default='')
    hits = models.IntegerField(default=0)
    hit_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='copy_vars')

    class Meta:
        ordering = ['-hits']

    @classmethod
    def create(cls, name, word):
        if cls.objects.filter(name=name):
            return None
        snake = name.replace(' ', '_')
        pascal = name.title().replace(' ', '')
        camel = pascal[0].lower() + pascal[1:]
        res = cls(name=name, word=word, snake=snake, camel=camel, pascal=pascal)
        res.save()
        return res

    @property
    def update_hits(self):
        self.hits += 1
        self.save()

    def __str__(self):
        return f"{self.word.kr_word} > {self.name}"

    def __repr__(self):
        return f"{self.word.kr_word} > {self.name}"
