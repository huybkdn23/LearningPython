import random
def histogram(s):
    d = dict()
    for x in s:
        d[x] = d.get(x, 0) + 1
    return d

def choose_from_hist(d):
    total = sum(d.values())
    element_random = random.choice(list(d.items()))
    return (element_random[0], element_random[1] * 100 / total)

hist =  histogram('abcaa')
print(choose_from_hist(hist))