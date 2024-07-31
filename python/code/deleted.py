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
    c=str(x)
    if counts(int(c), 1, 0) % 2 == 1:
       collected.append(c)
print(collected)
