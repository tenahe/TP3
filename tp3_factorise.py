def moy(liste):
    s = 0
    for i in liste:
        s += i
    if len(liste) == 0:
        return 0
    else:
        moy = s/len(liste)
        return (moy)

def sup(liste):
    s = 0
    for i in liste:
        s += i
    if len(liste) == 0:
        return 0
    else:
        moy = s/len(liste)
    cptr = 0
    for i in liste:
        if i > moy:
            cptr += 1
    return cptr

def inf(liste):
    s = 0
    for i in liste:
        s += i
    if len(liste) == 0:
        return 0
    else:
        moy = s / len(liste)
    cptr = 0
    for i in liste:
        if i < moy:
            cptr += 1
    return cptr