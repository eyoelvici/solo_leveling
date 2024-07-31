fruit='bananas'
x = 0
c = len(fruit)
flist=list([])
while x<c:
    spelling=str(fruit[c-1-x])
    flist.append(spelling)
    x+=1
print(flist)