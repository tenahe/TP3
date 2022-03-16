import tp3, unittest


class mytest(unittest.TestCase):
    # faire tourner le code de production tp3 à la main    
    def test_moy_sup_inf(self):
        liste = [2,4,20,9,1]
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((7.2,2,3),L)

    def test_moy_sup_inf2_1element(self):
        liste = [1]
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((1,0,0),L)

    def test_moy_sup_inf_negatif(self):
        liste = [-2,-3]
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((-2.5,1,1),L)
        #fail: tp3_factorise.sup differents

    def test_moy_sup_inf_negatif2(self):
        liste = [-2,-10,-3]
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((-5,2,1),L)

    def test_moy_sup_inf_1elementNull(self):
        liste = [0]
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((0,0,0),L)

    def test_moy_sup_inf_listeVide(self):
        liste = []
        L = tp3.moy_sup_inf(liste)
        self.assertEqual((0,0,0),L) 
        #error: division par 0

if __name__ == "__main__":
    unittest.main()

#problémes repérés : liste vide, moyenne arrondie



