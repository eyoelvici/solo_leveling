text='to-be-the-greatest-you-have-to-adapt-the-meaning-is-still-unclear-its-frrls-like-am-in-the-fog'
delimiter='-'
text_list=text.split(delimiter)
rejoined=delimiter.join(text_list)
text_list.sort()
print(text_list)


selected=[]
for i in range(len(text_list)):
    if len(text_list[i])>2 :
        selected.append(text_list[i])
print(f'the new collection of words are {selected}')




numbers='1,22,3,21,7,4,88,435,245,86,74,34,13,9,0,52,78,93'

# ------------------
# creat list from a string and if summation of each indexs value is odd then give it to new list
# ------------------

numb = [1, 39, 86, 1232, 345, 739]
collected = []


def counts(x, y, s):
    c = int(int(x)/10)
    reminder = int(x) % 10
    s = s+reminder
    if c > 0:
        return counts(c, y+1, s)
    else:
        return s


for x in numb:
    c = str(x)
    if counts(int(c), 1, 0) % 2 == 1:
       collected.append(c)
print(collected)
