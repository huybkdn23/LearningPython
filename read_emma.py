import string
import random
def process_file(filename):
    '''
    This function read the file
    and return a histogram of the words in the file
    '''
    hist = dict()
    fin = open(filename)
    for line in fin:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace).lower()
        hist[word] = hist.get(word, 0) + 1

def most_common(hist):
    t = []
    for word, n in hist.items():
        t.append((n, word))
    t.sort(reverse=True)
    return t
def random_word(hist):
    return random.choice(list(hist))

def substract(dict1, dict2):
    # result = dict()
    # for key in dict1:
    #     if key not in dict2: result[key] = None
    # return result
    return set(dict1).difference(dict2)
    #: or we can use set(dict1) - set(dict2)

hist = process_file('emma.txt')
words = process_file('words.txt')
# print(substract(hist, words))
print(random_word(hist))