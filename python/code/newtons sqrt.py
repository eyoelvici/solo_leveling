insert=int(input('> '))


def newtonsqrt(inse):
    n=5
    x = insert/2
    while n>0:
       sqr=(x+inse/x)/2
       x=sqr
       n-=1
    return sqr
print(newtonsqrt(insert))
    