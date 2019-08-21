import math
def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)

def estimate_pi():
    constant = 2 * math.sqrt(2) / 9801
    k = 0
    sum = 0
    while True:
        numerator = factorial(4 * k) * (1103 + 26390 * k)
        denominator = (factorial(k)**4 * 396**(4 * k))
        tmp = numerator / denominator
        sum += tmp
        if tmp < 1e-6: break
        k += 1
    return 1 / (sum * constant)

print(estimate_pi())
string = 'hagshjdg'
print(string[:])
string = 'huyhuy'
print(string[:])