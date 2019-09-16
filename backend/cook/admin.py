from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'wrong', 'short', 'slice', 'sound')


admin.site.register(Recipe, RecipeAdmin)
