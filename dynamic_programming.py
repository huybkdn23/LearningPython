import time

known = dict({0: 1, 1: 1})
def fibo_default(n):
    if n == 0 or n == 1: return 1
    else: return fibo_default(n - 1) + fibo_default(n - 2)

def fibo_dynamic(n):
    if n in known: return known[n]
    known[n] = fibo_dynamic(n-1) + fibo_dynamic(n-2)
    return known[n]

start = time.time()
print(fibo_default(500))
print(time.time() - start, 'seconds')

start = time.time()
print(fibo_dynamic(500))
print(time.time() - start, 'seconds')
