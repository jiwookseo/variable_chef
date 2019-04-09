preposition = {'in', 'at', 'into', 'out', 'on', 'for', 'to', 'from'}
article = {'a', 'an', 'the'}
conjunction = {'and', 'but', 'or', 'nor', 'so', 'for', 'yet', 'of', 'by'}
exclude = preposition.union(article).union(conjunction)


def rcp1(string):
    string = string.split()
    res = [word for word in string if word not in exclude]
    return " ".join(res)


def rcp2(string):
    string = string.split()
    res = [word[:3] for word in string]
    return " ".join(res)
