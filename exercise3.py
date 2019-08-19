def check_fermat(a, b, c, n):
    if n > 2:
        return False
    elif (a**n + b**n) == c**n:
        return True
    return False

def is_triangle(a, b, c):
    if (a + b > c) or (a + c > b) or (b + c > a):
        return True
    return False

a = int(input('Type a: '))
b = int(input('Type b: '))
c = int(input('Type c: '))
n = int(input('Type n: '))
if check_fermat(a, b, c, n):
    print('Fermat was right!')
else:
    print('Holy smokes, that\'s doesn\'t work')
if is_triangle(a, b, c):
    print('This is a triangle')
else:
    print('This is not a triangle')