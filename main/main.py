"""
main file handles input and output of the program, also handles main working process
"""

# imports
from classes import Network
from classes import Device

if __name__=='__main__':
    # print ('--DEBUG--')
    # for commutator in test_commutators:
    #     print (commutator)

    # main algorithm
    the_network = Network(10) # create network

    while 1:
        try:
            option = (int(input('Enter # of root device:\t')))
        except:
            continue
        break


    # ---DEBUG---
    # the_network.tag_root(9)
    print (the_network)
    the_network.STP(option)
    print (the_network)
    # print (the_network)
