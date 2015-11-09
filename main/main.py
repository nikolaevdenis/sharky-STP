"""
main file handles input and output of the program, also handles main working process
"""

# imports
from classes import Commutators
from classes import Device
# from random import randint


the_network = Commutators(10)

the_network.tag_root(9)
print (the_network)
# print (the_network.is_connected(1, 9))