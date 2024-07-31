import random
c=[]
for x in range(20):
    i=random.randint(1,10)
    c.append(i)
for x in range(20):
    i = random.randint(1, 10)
    c.append(i)
print(c)
dic=dict()
for x in c:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1
print(dic)