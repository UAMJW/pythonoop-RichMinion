class Toy:
    num = 0
    def __init__(self, name, kind, *args):
        self.name = name
        self.kind = kind
        self.data = args
        self.num = Toy.num
        Toy.num += 1

    def __repr__(self):
        return ' '.join([self.name,self.kind,str(self.num)])

    def playWith(self):
        print (self)

def getNewToy(name, kind):
    return Toy(name, kind)

t1 = Toy('Suzie', 'doll')
t2 = getNewToy('Jack', 'robot')
print (t1)
t2.playWith()