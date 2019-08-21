def nested_sum(array):
    '''
    Like reduce(func, list)
    func takes  takes two parameters of the form func (arg1, arg2) 
    where arg1 is the calculation result with the preceding elements, 
    arg2 is the value of the element of the list being calculated.
    ***Note: In python 3 reduce function is moved to "functools" package
    '''
    sum = 0
    for element in array:
        if isinstance(element, list):
            sum += nested_sum(element)
        else:
            sum += element
    return sum

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(array):
    '''
    Like map(func, list)
    '''
    newNested = []
    for element in array:
        if isinstance(element, list):
            newNested.append(capitalize_all(element))
        else: newNested.append(element.capitalize())
    return newNested

def only_upper(array):
    '''
    Like filter(func, list)
    '''
    res = []
    for element in array:
        if element.isupper(): res.append(element)
    return res

print(nested_sum([2, [1, 3, 4], 5, [6, 7], [8, 9, 10]]))
print(capitalize_nested(['huy', ['ho', 'Bach khoa', 'da Nang'], 'hai Chanh', ['Hai', 'lang'], ['quang', 'tri', '16t2']]))
print(only_upper(['da', 'NANG', 'La', 'thaNh', 'phO', 'DANG', 'SONG']))

'''
Exercise Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For
example, the cumulative sum of [1, 2, 3] is [1, 3, 6] .
'''
start = 0
end = 10
array = list(range(start, end + 1))
def sigma(numbers):
    sums = []
    total = 0
    for i in numbers:
        total += i
        sums.append(total)
    print(sums)

sigma(array)
'''
'''