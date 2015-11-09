"""
classes file implies all classes, which will be used in current program
"""

class Commutator:
    def __init__(self, endpoint, port, own_number):
        # commutator is performed as list in form
        # [0] - the number of this commutator
        # [1] - the number of routed commutator
        # [2] - port leading to routed commutator
        try:
            self.data.append([own_number, endpoint, port])
        except:
            self.data = [[own_number, endpoint, port]]
    def __str__(self):
        in_string = ''
        for item in self.data:
            in_string += 'Commutator #' + str(item[0]) \
                        + '\troutes to #' + str(item[1])\
                        + '\tthrough port #' + str(item[2]) + '\n'
        return in_string
