
def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    n, m: non-negative integers
    """
    if m < 0 or n < 0:
        return 'm&n have to be a non-negative integers'
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

print(ackermann(3, 6))