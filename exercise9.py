def is_matches(word1, word2):
    return word1 == word2

def bisect(lst, word):
    tmp = lst
    while True:
        mid = int(len(tmp) / 2)
        if word > tmp[mid]: 
            tmp = tmp[mid:]
        elif word < tmp[mid]: 
            tmp = tmp[:mid]
        elif word == tmp[mid]: return lst.index(word)
        
        if len(tmp) == 1: 
            if word == tmp[:]: return lst.index(word)
            else: return None
            
myList = ['huy', 'huy', '16T2', 'BKDN', 'c', 'jhfdg', '9792834', '87oinflksdf', '2873s', '123456']
myList.sort()
print(myList)
print(bisect(myList,'87oinflksdf'))