import numpy as np

# seznam iz lista
seznam_0 = np.array([1,2,3,4,5])
print("iz lista", seznam_0)

# seznam iz range-a
seznam_1 = np.array(range(6,10))
print("iz range-a", seznam_1)

# seznam ničel
seznam_2 = np.zeros(5)
print("seznam ničel", seznam_2)

# seznam enic
seznam_3 = np.ones(5)
print("seznam enic", seznam_3)

# naključna števila
seznam_4 = np.random.random(5)
print("random", seznam_4)

# naključen seznam z normalno porazdelitvijo
seznam_5 = np.random.randn(5)
print("normalna porazdelitev", seznam_5)

# seznam z enakomernim razmakom med številkami 
seznam_6 = np.linspace(0, 10, 3)
print("enakomeren razmak", seznam_6)

# seznam z arange
seznam_7 = np.arange(0, 11, 2)
print("arange", seznam_7)

# prazen seznam
seznam_8 = np.empty(4)
print("prazen seznam", seznam_8)

# predpisana vrednost
seznam_9 = np.full(5,1.)
print("predpisana vrednost", seznam_9)