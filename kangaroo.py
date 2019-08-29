class Kangaroo():
    """a Kangaroo is a marsupial"""
    # In this case that means that when __init__ is defined,
    # [] gets evaluated and contents gets a reference to
    # an empty list.
    
    # def __init__(self, contents=[]):
    #     """initialize the pouch contents; the default value is
    #     an empty list"""
    #     self.pouch_contents = contents

    def __init__(self, contents = None):
        if contents == None: self.pouch_contents = []
        else: self.pouch_contents = contents

    def __str__(self):
        """return a string representaion of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)
print(kanga)
print(roo)
# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.