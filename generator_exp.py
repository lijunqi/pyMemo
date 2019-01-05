import sys

'''
# memory
n = 10000000
a_list = [1 for i in range(n)]
a_gene = (1 for i in range(n))

print sys.getsizeof(a_list) # 40764032 bytes
print sys.getsizeof(a_gene) # 40 bytes
'''

rows =  [4, 2, 1, 5, 6]
seats = ['a', 's', 'd', 'f', 'q']

def foo():
    for row in rows:
        for s in seats:
            yield (row, "{}".format(s))

from pprint import pprint as pp
#pp(sorted(foo()))

gb = foo()
pp(next(gb)) # (4, 'a')
pp(next(gb)) # (4, 's')
