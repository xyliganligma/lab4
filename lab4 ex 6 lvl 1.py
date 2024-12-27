import random as rd
n,m=4,7
a=[[rd.randrange(0,100) for x in range(m)] for y in range (n)]
print(a)
j=[min(a[b]) for b in range(len(a))]
for k in range (n):
    print("{0:>5d}".format(j[k]), end='')