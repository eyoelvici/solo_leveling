number=[1,2,3,4,5,6]
a,b,c,d,e,f=number
print(a)
h,i,j,k,l,m=[*number]
i,j=h,l
print(h)
print(id(a) == id(h) == id(number[0]))