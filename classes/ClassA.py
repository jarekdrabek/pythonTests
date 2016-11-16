from ClassB import ClassB

class ClassA(object):
    def __init__(self):
        print "Constructing ClassA", __name__, __file__

    def message(self):
        ClassB().message()

ClassA().message()