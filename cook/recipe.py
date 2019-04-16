from .models import Recipe
from . import papago, google


def consonant(word):
    res = [word[0]] + [i for i in word[1:] if i not in {'i', 'e', 'o', 'u', 'a'}][:2]
    return "".join(res)


def cook(kr_word):
    ok, en_word = papago.translate(kr_word)
    gd = google.syntax_text(en_word)
    print(gd)
    if not ok:
        return False, None, None
    res = [[], [], [], []]
    check = None
    for word, tag in gd.items():
        if tag in {'PUNCT', 'DET', 'ADP'}:
            if word == 'of':
                check = len(res[0])
            else:
                continue
        recipe = Recipe.objects.filter(name=word).first()
        if not recipe:
            recipe = Recipe.create(name=word)
        word = recipe.wrong if recipe.wrong else word
        res[0].append(word)
        res[1].append(recipe.short if recipe.short else word)
        res[2].append(recipe.slice)
        res[3].append(recipe.sound)
    if check:
        for i in range(4):
            res.append(res[i][check + 1:] + res[i][:check])
    res = [' '.join(i) for i in res if i]
    res[1:] = list(set(res[1:]))
    return True, res[0], res[1:]
