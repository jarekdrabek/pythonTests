from collections import defaultdict
from itertools import izip

dictionary = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

print "\nKEYS:"
for k in dictionary.keys():
    print k

print "\nVALUES:"
for v in dictionary.values():
    print v

print "\nDELETING:"
for k in dictionary.keys():
    if k.startswith('m'):
        del dictionary[k]
print dictionary

dictionary = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
print "\nBOTH Key AND Value:"
for k,v in dictionary.items():
    print k,"-->",v

dictionary = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
print "\nBOTH Key AND Value with ITERITEM:"
for k,v in dictionary.iteritems():
    print k,"-->",v

print "\nCREATING DICTIONARY with ZIP:"
names = {'matthew', 'rachel', 'raymond'}
colors = {'blue', 'green', 'red'}
d = dict(izip(names, colors))
print d

print "\nCOUNTING with DICTIONARIES:"
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = {}
for col in colors:
    d[col] = d.get(col, 0) + 1
print d

print "\nDEFAULTDICT example:"
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = defaultdict(int)
for col in colors:
    d[col] += 1
print d

print "\nSETDEFAULT - GROUPING dict values example: @DEPRECATED"
names = ['Marek', 'Jacek', 'Jan', 'Tomasz', 'Lukasz', 'Marian']
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
print d

# the same is possible with defaultdict
dd = defaultdict(list)
for name in names:
    key = len(name)
    dd[key].append(name)
print dd
