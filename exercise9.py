def is_matches(word1, word2):
    return word1 == word2

def bisect(lst, word):
    mid = int(len(lst) / 2)
    if mid < 0: return
    if word[0] > lst[mid][0]: return bisect(lst[mid + 1:], word)
    elif word[0] < lst[mid][0]: return bisect(lst[:mid - 1], word)
    elif word[0] == lst[mid][0] and is_matches(word, lst[mid]): return mid

myList = ['huy', 'huy', '16T2', 'BKDN', 'c']
myList.sort()
print(myList)
print(bisect(myList, 'c'))