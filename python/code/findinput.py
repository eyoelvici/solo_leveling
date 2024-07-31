sent = 'the moon shine bright in the dark'
find = input('> ')
end = len(find)

begin = 0

while begin < (len(sent) - len(find) + 1):
    if sent[begin:end] == find:
        output = f'sent[{begin}:{end}]'
        print(output)
        begin += 1
        end+=1
    else:
        begin += 1
        end += 1
sent_lists=[]

for x in sent:
    sent_lists.append(x)
print(sent_lists)