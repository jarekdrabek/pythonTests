import logging

class ClassB(object):
    def __init__(self):
        print "Constructing ClassB", __name__, __file__

    def message(self):
        print "Outputting message", __name__, __file__


