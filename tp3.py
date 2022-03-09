def nb_moyenne(t):
    a=0
    b=0
    c=0
    d=0
    for i in range(len(t)):
        a+=t[i]
    b=int(a/len(t))
    for i in range(len(t)):
        if t[i]>b:
            c+=1
    for i in range(len(t)):
        if t[i]<b:
            d+=1
    return b, c, d