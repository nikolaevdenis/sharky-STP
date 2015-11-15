"""
main file handles input and output of the program, also handles main working process
"""

# imports
from classes.network import Network

# menu functions
def prompt_quantity(default_quantity = 10):
    # prompting quantity of devices
    while 1:
        option_nodes_quantity = input('Enter quantity of devices:\t')
        if option_nodes_quantity == '':
            option_nodes_quantity = default_quantity
            break
        try:
            option_nodes_quantity = int(option_nodes_quantity)
        except:
            continue
        break
    return option_nodes_quantity

def prompt_root_number(default_root = 5):
    # prompting # of root device
    while 1:
        option_root_number = input('Enter # of root device:\t')
        if option_root_number == '':
            option_root_number = default_root
            break
        try:
            option_root_number = int(option_root_number)
        except:
            continue
        break
    return option_root_number

# MAIN part
if __name__=='__main__':

    # menu
    nodes_quantity = prompt_quantity(20)
    root_number = prompt_root_number(0)

    # main algorithm
    the_network = Network(nodes_quantity)
    print (the_network)
    the_network.STP(root_number)
    print (the_network)