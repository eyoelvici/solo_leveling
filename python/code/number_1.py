import math

radx=int(input('input raduis: '))
area=float(radx*radx*math.pi)
print(area)


for u in range(0,11):
    for y in range(0,11):
        if u % 5 ==0:
            if  y%5 == 0:
                print('+',end='')
            else:
	            print('-',end='')
print()

