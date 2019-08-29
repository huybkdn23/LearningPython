def histogram(string):
    d = dict()
    for value in string:
        if value not in d: d[value] = 1
        else: d[value] += 1
    return d

def reverse_loopkup(d, n):
    result = dict()
    for key in d:
        if d[key] == n: result.update({key: d[key]})
    if len(result): return result
    raise ValueError('The value does not appear in the dictionary')

def invert_dict(d):
    result = dict()
    for key in d:
        val = d[key]
        if val not in result: result[val] = [key]
        else: result[val].append(key)
    return result
    

myDict = dict({
    'one':'huy', 
    'two': 'Ho', 
    'three': '16T2',
    1: [1,2,3,5,5],
})
print(myDict)

myDict2 = histogram('dai hoc bach khoa - dai hoc da nang')
print(reverse_loopkup(myDict2, 6))
print(myDict2)
print(invert_dict(myDict2))