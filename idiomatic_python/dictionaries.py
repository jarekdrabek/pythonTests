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
