import tp3_factorise, unittest

class Mytest(unittest.TestCase):
    def test_moy(self):
        liste =  [2,4,20,9,1]
        m = tp3_factorise.moy(liste)
        self.assertEqual(7.2,m)

    def test_moy_1element(self):
        liste = [1] 
        m = tp3_factorise.moy(liste)
        self.assertEqual(1,m)
    
    def test_sup(self):
        liste = [2,4,20,9,1]
        sup = tp3_factorise.sup(liste)
        self.assertEqual(2,sup)
    
    def test_inf(self):
        liste = [2,4,20,9,1]
        inf = tp3_factorise.inf(liste)
        self.assertEqual(3,inf)


if __name__ == "__main__":
    unittest.main()