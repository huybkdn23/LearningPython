
def first(word):
    """Returns the first character of a string."""
    return word[0]


def last(word):
    """Returns the last character of a string."""
    return word[-1]


def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

def is_power(a, b):
    if a < b:
        return False
    elif a == b:
        return True
    return is_power(a/b, b)

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

if is_power(9,3):
    print('YES')
else:
    print('NO')
print(GCD(4,6))
print(is_palindrome('allen'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))
print(is_palindrome('house'))