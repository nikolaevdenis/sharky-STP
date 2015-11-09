"""
main file handles input and output of the program, also handles main working process
"""

# imports
from classes import Commutators
from classes import Device


# print ('--DEBUG--')
# for commutator in test_commutators:
#     print (commutator)

# main algorithm
the_network = Commutators(10) # create network

# prompt to set root device
while 1:
    try:
        the_network.tag_root(int(input('Enter # of root device:\t')))
    except:
        continue
    break


# ---DEBUG---
# the_network.tag_root(9)
# print (the_network)
# print (the_network.is_connected(1, 9))