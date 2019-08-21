def is_palindrome(number, start, length):
    '''
    Check the number is palindrome
    '''
    numParseToString = str(number)[start:start + length]
    return numParseToString == numParseToString[::-1]

def check_condition(number):

    '''
    Condition is that first, if the last digits were palindromic
    and then the last 5 numbers of number+1 were palindromic
    and then the middle 4 out of 6 number+2 were palindromic
    and finally all 6 were palindromic
    => return the number valid
    '''
    return (is_palindrome(number, 2, 4) and 
            is_palindrome(number + 1, 1, 5) and 
            is_palindrome(number + 2, 1, 4) and 
            is_palindrome(number + 3, 0, 6))
    
def find():
    for number in range(100000, 1000000):
        if check_condition(number):
            print(number)

find()