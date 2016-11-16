import unittest
import mock
# from mock import MagicMock
# from mock import Mock

class ClassA:
    def __init__(self, other_class):
        self.otherClass = other_class

    def printA(self):
        if self.otherClass.shouldPrint():
            print "ClassA Printing"
        else:
            print "Nothing to print KURWA!"

class ClassB:
    def shouldPrint(self):
        return True


class BackupNamingTest(unittest.TestCase):

    def testTest(self):
        b = ClassB()
        # b.shouldPrint = MagicMock(return_value=False)
        b.shouldPrint = lambda : False
        # b.printB
        ClassA(b).printA()

if __name__ == '__main__':
    unittest.main()