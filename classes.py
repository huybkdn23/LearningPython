#: c01:SimpleClass.py
class Simple:
    'Simple class'
    def __init__(self, str):
        print ('Inside the Simple constructor')
        self.s = str
    # Two methods:
    def show(self):
        print (self.s)
    def showMsg(self, msg):
        print (msg + ':'),
        self.show() # Calling another method)
    def sum(self, a, b):
        print(a+b)
if __name__ == "__main__":
    # Create an object:
    x = Simple("constructor argument")
    x.show()
    x.showMsg("A message")
#:~