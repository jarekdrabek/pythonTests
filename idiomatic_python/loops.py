#FOR with ELSE
colors = ['red', 'blue', 'green', "violet"]
def find(sequence, target):
    print "\nFOR with ELSE:"
    for i, item in enumerate(sequence):
        if target in item:
            break
    else:
        return -1
    return i

print find(colors, "ee")
print find(colors, "ble")

#ITERATOR EXAMPLE
print "\nITERATOR EXAMPLE:"
colors = ['red', 'blue', 'green', "violet"]
for block in iter(colors):
    if "ee" not in block:
        print block

# iter(...)
# iter(collection) -> iterator
# iter(callable, sentinel) -> iterator


#CUSTOM SORT ORDER
print "\nCUSTOM SORT ORDER:"
colors = ['red', 'blue', 'green', "violet"]
for col in sorted(colors, key=len):
    print col

#looping by reverse sorted order
print "\nLOOPING BY REVERSE SORTED ORDER:"
colors = ['red', 'blue', 'green']
for col  in sorted(colors, reverse=True):
    print col

#looping by sorted order
print "\nLOOPING BY SORTED ORDER:"
colors = ['red', 'blue', 'green']
for col  in sorted(colors):
    print col

#IZIP (in favor of ZIP, operates on iterator, not creating the whole lista at the time)
from itertools import izip
colors = ['red', 'blue', 'green']
names = ['rachel', 'ben', 'mark', 'tom']
print "\nIZIP:"
for col, name in izip(colors, names):
    print name, '-->', col

#ZIP (it creates the dictionary in advance)
colors = ['red', 'blue', 'green']
names = ['rachel', 'ben', 'mark', 'tom']
print "\nZIP:"
for col, name in zip(colors, names):
    print name, '-->', col

#LOOPING OVER A COLLECTION AND INDICIES
print "\nLOOPING OVER A COLLECTION AND INDICIES:"
for i, col in enumerate(colors):
    print "%s --> %s"%(i, col)

#REVERSED
print "\nREVERSED:"
for col in reversed(colors):
    print col

#foreach
print "\nFOREACH:"
for col in colors:
    print col

#range
print "\nRANGE:"
for i in range(6):
    print i

#xrange - it does not create table elements at the beginning
print "\nXRANGE:"
for i in xrange(6):
    print i



