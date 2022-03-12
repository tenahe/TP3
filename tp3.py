def nb_moyenne(t):
    a=0
    b=0
    c=0
    d=0
    for i in range(len(t)):
        a+=t[i]
    #rajout de if pour liste vide
    if len(t)==0:       
        return 0,0,0
    else:
        b=(a/len(t))
        #conversion du int en float pour bien déterminer inf st sup
        for i in range(len(t)):
            if t[i]>b:
                c+=1
        for i in range(len(t)):
            if t[i]<b:
                d+=1
        return b, c, d