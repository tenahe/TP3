def moy_sup_inf(liste):
    somme = 0
    moy = 0
    sup = 0
    inf = 0
    for i in range(len(liste)):
        somme += liste[i]
    #rajout de if pour liste vide
    if len(liste) == 0:       
        return 0,0,0
    else:
        moyenne = (somme/len(liste))
        #conversion du int en float pour bien déterminer inf st sup
        for i in range(len(liste)):
            if liste[i] > moyenne:
                sup += 1
        for i in range(len(liste)):
            if liste[i] < moyenne:
                inf += 1
        return moyenne, sup, inf