"""
classes file implies all classes, which will be used in current program
"""

class Commutator:
    def __init__(self, endpoint, port, own_number):
        # commutator is performed as list of tuples (endpoint, port used)
        self.data = [(endpoint, port)]
        self.number = own_number
    def append(self, endpoint, port):
        if all(item[1] != port for item in self.data):
            self.data.append((endpoint, port))
    def __str__(self):
        in_string = 'Commutator #' + str(self.number) + '\n'
        for item in self.data:
            in_string += '\troutes to #' + str(item[0]) + \
                         ' \tover port #' + str(item[1]) + '\n'
        return in_string