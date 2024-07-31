import math
numb=int(input('inpout integer: '))

def mysqrt(a):
    c=10
    h1 = a/3
    while c>0:
        soln=((h1+a/h1)/2)
        h1=soln
        c-=1
    return soln
print("a   mysqrt(a)   math.sqrt(a)   diff")
print("-   ---------   ------------   ----")
c=10
while c>0:
    diff = abs(math.sqrt(c)-mysqrt(c))
    math.sqrt(c)
    print(f"{c:4}  {mysqrt(c):15f}  {math.sqrt(c):15f}  {diff:40f}")
    c=c-1