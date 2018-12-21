import sys

n = 10000000
a_list = [1 for i in range(n)]
a_gene = (1 for i in range(n))

print sys.getsizeof(a_list) # 40764032 bytes
print sys.getsizeof(a_gene) # 40 bytes
