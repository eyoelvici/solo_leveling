numbers='numbers.txt'
#access file called numbers.txt
numbez=open(numbers)
numbers_list=numbez.read()
lis=numbers_list.split('\n')
gtwothousedn=[]
def fliters(y):
    for x in y:
        x=int(x)
        if x > 2000:
            gtwothousedn.append(x)
    return gtwothousedn
print(fliters(lis))
