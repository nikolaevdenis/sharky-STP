"""
classes file implies all classes, which will be used in current program
"""
class Commutators:

    def __init__(self, max):
        self.network = []
        for i in range(max):
            self.network.append(Device(0, 0, i))
            for j in range(max):
                self.network[i].append(j, j)

    def __str__(self):
        in_string = ''
        for item in self.network:
            in_string += str(item) + '\n'
        return in_string

    def is_connected(self, startpoint, endpoint):
        # checks if the startpoint commutator is connected to endpoint
        # if yes, returns a connection port
        # if no, returns False
        return self.network[startpoint].is_connected(endpoint)

    def tag_root(self, device_number):
        self.network[device_number].set_root()

class Device:

    def __init__(self, endpoint, port, own_number):
        # commutator is performed as list of tuples (endpoint, port used)
        self.data = [(endpoint, port)]
        self.number = own_number
        self.is_root = False

    def append(self, endpoint, port):
        if all(item[1] != port for item in self.data):
            self.data.append((endpoint, port))

    def __str__(self):
        in_string = 'Commutator #' + str(self.number) + '\n'
        for item in self.data:
            in_string += '\troutes to #' + str(item[0]) + \
                         ' \tover port #' + str(item[1]) + '\n'
        if self.is_root:
            in_string += '\t----ROOT----\n'
        return in_string

    def is_connected(self, endpoint):
        # checks if the current commutator is connected to endpoint
        # if yes, returns a connection port
        # if no, returns False
        for item in self.data:
            if item[0] == endpoint:
                return item[1]
        else:
            return False

    def set_root(self):
        self.is_root = True