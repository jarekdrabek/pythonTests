from functools import partial

f = open('file1','r')
blocks = []
for block in iter(partial(f.read, 32),''):
    blocks.append(block)

print blocks