import random
'''
x=random.randrange(4,10,2)

print(x)

string_sentence= \'''the major talking point in every conversation is 
common selamta: like hey how you class life family work
get to know you part: how to???\'''
number_student=input('how many student are there?')
yy=int(number_student)+1
FullName='kahn yared'
name=FullName.split(' ')

for i in range(0,yy):
    student=[]
    student[i]=FullName
    FullName=input('enput full Name: ')

name[1]=name[1].replace(name[1],'dawit')
FirstName=name[0]
MiddleName=name[1]
print(name)

'''
quantity = 3
itemno = 567
price = 49.95
myorder = f"I want {quantity} pieces of item {itemno} for {price} dollars."
print(myorder)
print(FullName)
print(name)
for xy in name:
	print(xy)
'''
print(len(string_sentence))

print(string_sentence)

print(string_sentence[10:14])

'''
if 'major' in string_sentence:
    print('present')

elif 'potato':
    print('present')

else:
    print('not present')