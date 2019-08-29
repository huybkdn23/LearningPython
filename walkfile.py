import os

def walk(dirname):
    '''
    Prints the names of all files in dirname and in its subdirectories
    dirname: string name of directory

    That's function of self-definition
    '''
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path): print(path)
        else: walk(path)

def walk2(dirname):
    '''
    Prints the names of all files in dirname and in its subdirectories
    dirname: string name of directory

    That's function uses  walk() function of os nodule
    '''
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))

if __name__ == "__main__":
    walk('.')
    print('<--------------------------------------------------------------------------------------------------------------->')
    walk2('.')