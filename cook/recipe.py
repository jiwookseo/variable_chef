from .models import Recipe
from . import papago, google

preposition = {'in', 'at', 'into', 'out', 'on', 'for', 'to', 'from'}
article = {'a', 'an', 'the'}
# conjunction = {'and', 'but', 'or', 'nor', 'so', 'for', 'yet', 'of', 'by'}
exclude = preposition.union(article)


def rcp(string):
    string = string.split()
    res = [word for word in string if word not in exclude]
    return res


def consonant(word):
    res = [word[0]] + [i for i in word[1:] if i not in {'i', 'e', 'o', 'u', 'a'}][:2]
    return "".join(res)


def cook(kr_word):
    ok, en_word = papago.translate(kr_word)
    print(google.syntax_text(en_word))
    if not ok:
        return False, None, None
    res = [[], [], [], []]
    for word in rcp(en_word):
        recipe = Recipe.objects.filter(name=word).first()
        if not recipe:
            recipe = Recipe.create(name=word)
        word = recipe.wrong if recipe.wrong else word
        res[0].append(word)
        res[1].append(recipe.short if recipe.short else word)
        res[2].append(recipe.slice)
        res[3].append(recipe.sound)
    for i in range(4):
        j = None
        if res[i].count('of'):
            j = res[i].index('of')
        if j:
            res.append(res[i][j + 1:] + res[i][:j])

    res = [' '.join(i) for i in res if i]
    res[1:] = list(set(res[1:]))
    print(res[0])
    return True, res[0], res[1:]
