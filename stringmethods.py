def count(string, sub, start = 0, end = -1):
    if end < 0: end = len(string)
    count, index = 0, 0
    for i in range(start, end):
        index = find(string, sub, index, end)
        # print(i)
        if index < 0: 
            return count
        count += 1
        index += 1

def find(string, sub, start = 0, end = -1):
    if end < 0: end = len(string)
    for i in range(start, end):
        check = False
        if sub == string[i : i + len(sub)]: 
            check = True
        if check: return i
    return -1

print(count('huyababab1235cece16T2', '1'))
print(find('huyabcde16T2aa', 'a', 4))