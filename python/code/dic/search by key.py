dic={'name':'joshep','age':'15','grade':'10'}
find=input('> ')
for key,value in dic.items():
    if key == find:
        print(value)

#list of tuple
t=('name','age','year')
print(t[-1])