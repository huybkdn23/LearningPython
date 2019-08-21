import math
import decimal
import fractions
decimal.getcontext().prec = 10
def test_square_root(n):
    pow = 0
    result = 0
    x = n
    while x > 100:
        x /= 100
        pow += 2
    if x < 10:
        x = 2 * 10**pow
    else:
        x = 6 * 10**pow
    while True:
        result = 1/2 * (x + n/x)
        if x == result:
            return result
        x = result

def eval_loop():
    while True:
        string = input('Type a number to get square root(type \'done\' to exit): ')
        if string == 'done':
            print('DONE!')
            break
        print(eval(string))
        

for number in range(1, 10):
    squareRoot = test_square_root(number)
    mathSqrt = math.sqrt(number)
    print('%.1f\t%.11f\t%.11f\t{}\n'.format(math.fabs(mathSqrt - squareRoot)) %(number, squareRoot, mathSqrt))

eval_loop()
