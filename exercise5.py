import re
fin = open('words.txt')
print(fin.read())
#: after function call readline(), the pointer is moved to the next line
for line in fin:
    print('for loop')
    print(line.strip())

def split(string):
    return re.split(r'\s+', string.strip())

def has_no_e(word):
    if 'e' not in word and 'E' not in word: return True
    return False

def words_no_e(string):
    split_string = split(string)
    words = []
    for word in split_string:
        if has_no_e(word):
            words.append(word)
    return words

def percentage_no_e(string):
    listWordsNoE = words_no_e(string)
    return 100 * len(listWordsNoE) / len(split(string))

print(percentage_no_e('    uhww3kjrhwsekjhf    hwsejkfhekws  hfew fjeskf9srhqw rgww   '), '%')