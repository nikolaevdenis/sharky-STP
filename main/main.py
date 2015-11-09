"""
Main file handles input and output of the program, also handles main working process
"""

# imports
from classes import Commutator
from random import randint

test_commutators = Commutator(1, 1, 1)
for i in range(10):
    test_commutators.append(randint(0, 10), randint(0, 100))

print (test_commutators)