from django.db import models
from . import papago


class Word(models.Model):
    kr_word = models.CharField(max_length=100, unique=True)
    en_word = models.TextField()

    def translate(self):
        ok, translated = papago.translate(self.kr_word)
        if ok:
            self.en_word = translated

    def __str__(self):
        return f"{self.kr_word} : {self.en_word}"

    def __repr__(self):
        return f"{self.kr_word} : {self.en_word}"


class Variable(models.Model):
    name = models.TextField()  # lowercase split by space
    snake_case = models.TextField()
    camel_case = models.TextField()
    pascal_case = models.TextField()
    copy_hits = models.IntegerField(default=0)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    def set_snake(self):
        self.snake_case = self.name.replace(' ', '_')

    def set_camel(self):
        camel = self.name.title().replace(' ', '')
        camel = camel[0].lower() + camel[1:]
        self.camel_case = camel

    def set_pascal(self):
        self.pascal_case = self.name.title().replace(' ', '')

    def __str__(self):
        return f"{self.word.kr_word} > {self.name}"

    def __repr__(self):
        return f"{self.word.kr_word} > {self.name}"
