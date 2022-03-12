import tp3, unittest

def moy(t):
    s=0
    for i in t:
        s+=i
    if len(t)==0:
        return 0
    else:
        moy=s/len(t)
        return (moy)

def sup(t):
    s=0
    for i in t:
        s+=i
    if len(t)==0:
        return 0
    else:
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
    if len(t)==0:
        return 0
    else:
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
        #fail: sup differents

    def test_nb_moyenne4(self):
        t=[-2,-10,-3]
        L=tp3.nb_moyenne(t)
        self.assertEqual((moy(t),sup(t),inf(t)),L)

    def test_nb_moyenne5(self):
        t=[0]
        L=tp3.nb_moyenne(t)
        self.assertEqual((moy(t),sup(t),inf(t)),L)


    def test_nb_moyenne6(self):
        t=[]
        L=tp3.nb_moyenne(t)
        self.assertEqual((moy(t),sup(t),inf(t)),L) 
        #error: division par 0

if __name__ == "__main__":
    unittest.main()

#problémes repérés : liste vide, moyenne arrondie



