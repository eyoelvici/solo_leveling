'''
def has_no_e(filex):
    print()
'''

'''fin=open('word.txt')
for line in fin:
    if 'magic' in line:
        print(line)
'''

'''
Write a function named avoids that takes a word 
and 
a string of forbidden letters, 
and that returns Trueif 
the word doesn’t use any of 
the forbidden letters.
'''

def avoids(wrods,forbd):
    count=0
    for x in wrods:
        if x in forbd:
            return False
        else:
            count+=1
    print(count)
    return True

    
print(avoids('jack the ripear','aeiou'))

print(avoids('crypt', 'aeiou'))
