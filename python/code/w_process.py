import string
import matplotlib.pyplot as plt
'''
fin=open('word.txt')

for line in fin:
    
    if len(line)>19:
        print(line)


fin = open('word.txt')
for line in fin:
    word = line.strip()
    if len(word)>19:
        print(word)
'''


'''
with open('word.txt','r') as file:
    lines=file.read().strip()
    dictt = {}
    for word in lines:
        if word not in dictt:
            dictt[word] = 1
        else:
            dictt[word] += 1
print(dictt)
'''

with open('words2.txt', 'r',encoding='utf-8') as file:
    dfdf=[]
    defe={}
    lines = file.read()
    correction=(str.maketrans('', '',string.punctuation))
    lines=lines.translate(correction).lower().split()
    
    '''
    counter=0
    #for total number of words
    total_word=len(lines)
    print(total_word)
    
    # for unique words
    for x in lines:
        if x not in dfdf:
            dfdf.append(x)
    unii=len(dfdf)
    print(unii)
    
    # or other unique words or different words used in the book
    for x in lines:
        if x in defe:
            defe[x]+=1
        else:
            defe[x]=1
    print(len(defe))

    # word that only appear one time
    coo=0
    for y in defe:
        if defe[y]==1:
            coo+=1
    print(coo)
    
    
    # 20 most frequently-used words in the book.
    cvc=[]
    for value in defe.values():
        if value not in cvc:
            cvc.append(value)
    cvc.sort(reverse=True)

    for key,value in defe.items():
        if value>=cvc[20]:
            print(key)
    
    
    '''    
    #the histogram of words

    word_histo=dict()

    for x in lines:
        if x in word_histo:
            word_histo[x]+=1
        else:
            word_histo[x]=1
    
    list_value=[]
    cars=[]
    for valuee in word_histo.values():
        if valuee not in list_value:
            list_value.append(valuee)
        
    list_value.sort(reverse=True)   
frecc=list(word_histo.values())
plt.hist(list_value,bins=100,edgecolor='black')
plt.title('frequency')
plt.ylabel('number of words')
plt.show()

