# You are given a two lists A and B. Your task is to compute their cartesian product X.

A = [1, 2]
B = [3, 4]

#AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]

#Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order

from itertools import product
''''
for i in A:
    for j in B:
        print((i, j), end=" ")
'''
C = list(map(int,input().split()))
D = list(map(int,input().split()))

output = list(product(C,D))
#print(list(output))

for item in output:
    print(item, end=" ")
