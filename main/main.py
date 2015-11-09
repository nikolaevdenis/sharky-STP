"""
Main file handles input and output of the program, also handles main working process
"""

# imports
from classes import Commutator
from random import randint

test_commutators = []
for i in range(10):
    test_commutators.append(Commutator(i, i, i))
    for j in range(10):
        test_commutators[i].append(j, j)

for commutator in test_commutators:
    print (commutator)

print (test_commutators[0].is_connected(5))