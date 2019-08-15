def col70(s):
    print('{:>70}'.format(s))

def draw_table():
    print('{:<39} + {:-<6} + {:-^15} + {:->10} +'.format('', '', '', ''))
    print('{:<39} | {:<6} | {:^15} | {:>10} |'.format('', 'Id', 'Ho Ten', 'QueQuan'))
    print('{:<39} | {:<6} | {:^15} | {:>10} |'.format('', '001', 'Huy Ho', 'Quang Tri'))
    print('{:<39} | {:<6} | {:^15} | {:>10} |'.format('', '002', 'Nguyen A', 'Da Nang'))
    print('{:<39} + {:-<6} + {:-^15} + {:->10} +'.format('', '', '', ''))


def draw_grid():
    def same_code1():
        print('{:<18}{:^1}{:>18}'.format('|', '|', '|'))
    def same_code2():
        print('+'),
        for i in range(17):
            if i == 8:
                print('+'),
            else:
                print('-'),
        print('+')
    same_code2()
    for i in range(15):
        if i == 15/2:
            same_code2()
        same_code1()
    same_code2()
        
def do_twice(func, x):
    func(x)
    func(x)

def print_spam(s):
    print(s)

def print_twice(s):
    print(s),;print(s)

col70('Bach Khoa DN')
draw_table()
draw_grid()
do_twice(print_twice, 'akjsdh')