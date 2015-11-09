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
        test_commutators[i].append(randint(0, 10), 1)

for commutator in test_commutators:
    print (commutator)