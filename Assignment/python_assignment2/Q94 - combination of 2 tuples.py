#Q94. Write a Python program to get all combinations of 2 tuples.
#Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
#Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

import itertools

tup1 = (7, 2)
tup2 = (7, 8)
 
list_result = list(itertools.chain(list(itertools.product(tup1,tup2)),list(itertools.product(tup2,tup1))))

print(list_result)