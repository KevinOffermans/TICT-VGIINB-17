from numpy.matlib import *
from numpy.linalg import inv,solve
def printM(s,a):
    print(s+" = ("+("%d" %a.shape[0])+"x"+("%d" %a.shape[1])+")-matrix")
    rows = a.shape[0]
    cols = a.shape[1]
    for i in range(0,rows):
        for j in range(0,cols):
            print("%8.4f" %a[i, j], end=''),
        print("")
    print


# a=matrix('1 2 3; \
# 4 5 6')
# b=matrix('9 8 2; \
# 3 2 1')
# c=a*b.T
# printM('a',c)

y=matrix('5; 7')
a=matrix('3 2; \
          2 4')
x=inv(a)*y
printM('x',x)