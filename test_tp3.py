import tp3, unittest

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


class mytest(unittest.TestCase):
    '''def setup(self):
        self.liste=[2,4,20,9,1]
        self.L=tp3.moy_sup_inf(self.liste)

    def test_moy_sup_inf(self):
        self.assertEqual((moy(self.liste),sup(self.liste),inf(self.liste)),self.L)'''
        # essai setup raté
        
    def test_moy_sup_inf(self):
        liste = [2,4,20,9,1]
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((moy(liste),sup(liste),inf(liste)),L)

    def test_moy_sup_inf2_1element(self):
        liste = [1]
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((moy(liste),sup(liste),inf(liste)),L)

    def test_moy_sup_inf_negatif(self):
        liste = [-2,-3]
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((moy(liste),sup(liste),inf(liste)),L)
        #fail: sup differents

    def test_moy_sup_inf_negatif2(self):
        liste = [-2,-10,-3]
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((moy(liste),sup(liste),inf(liste)),L)

    def test_moy_sup_inf_1elementNull(self):
        liste = [0]
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((moy(liste),sup(liste),inf(liste)),L)

    def test_moy_sup_inf_listeVide(self):
        liste = []
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((moy(liste),sup(liste),inf(liste)),L) 
        #error: division par 0

if __name__ == "__main__":
    unittest.main()

#problémes repérés : liste vide, moyenne arrondie



