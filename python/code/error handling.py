#trying try to avoid error display
x=input("> ")

try :
    leng=len(x)
    print(x[leng])
except IndexError:
    print('hey buddy index is out of range')

try :
    x[0]='l'
except TypeError:
    print('cant add to string')