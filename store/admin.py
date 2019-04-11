from django.contrib import admin
from .models import Word, Variable


class WordAdmin(admin.ModelAdmin):
    list_display = ('kr_word', 'en_word',)


class VariableAdmin(admin.ModelAdmin):
    list_display = ('word', 'name', 'hits',)


admin.site.register(Word, WordAdmin)
admin.site.register(Variable, VariableAdmin)
