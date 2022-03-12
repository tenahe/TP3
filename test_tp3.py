import tp3, unittest

def moy(t):
    s=0
    for i in t:
        s+=i
    moy=s/len(t)
    return int(moy)

def sup(t):
    s=0
    for i in t:
        s+=i
    moy=s/len(t)
    cptr=0
    for i in t:
        if i>moy:
            cptr+=1
    return cptr

def inf(t):
    s=0
    for i in t:
        s+=i
    moy=s/len(t)
    cptr=0
    for i in t:
        if i<moy:
            cptr+=1
    return cptr


class mytest(unittest.TestCase):
    '''def setup(self):
        self.t=[2,4,20,9,1]
        self.L=tp3.nb_moyenne(self.t)

    def test_nb_moyenne(self):
        self.assertEqual((moy(self.t),sup(self.t),inf(self.t)),self.L)'''
        
    def test_nb_moyenne(self):
        t=[2,4,20,9,1]
        L=tp3.nb_moyenne(t)
        self.assertEqual((moy(t),sup(t),inf(t)),L)

    def test_nb_moyenne2(self):
        t=[1]
        L=tp3.nb_moyenne(t)
        self.assertEqual((moy(t),sup(t),inf(t)),L)

    def test_nb_moyenne3(self):
        t=[-2,-3]
        L=tp3.nb_moyenne(t)
        self.assertEqual((moy(t),sup(t),inf(t)),L)
        #fail: pas le même inf

    def test_nb_moyenne4(self):
        t=[0]
        L=tp3.nb_moyenne(t)
        self.assertEqual((moy(t),sup(t),inf(t)),L)

    def test_nb_moyenne5(self):
        t=[]
        L=tp3.nb_moyenne(t)
        self.assertEqual((moy(t),sup(t),inf(t)),L) 
        #error: division par 0

if __name__ == "__main__":
    unittest.main()



'''def verif(tableau):
    moy_sup_inf = tp3.nb_moyenne(tableau)
    print(moy_sup_inf)

tab=[2,4,20,9,1]
verif(tab)

tab2 = [0,0,0,0,0,32,0]
verif(tab2)'''

