"""
classes file implies all classes, which will be used in current program
"""
from random import randint

class Commutators:

    def __init__(self, max):
        # creates random network
        self.network = []
        self.root_number = None
        for i in range(max):
            self.network.append(Device(0, 0, i))
            for j in range(max):
                self.network[i].append(randint(0, j), randint(0, j))

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
        # tags the device as root, remember the root device number
        self.network[device_number].set_root()
        self.root_number = device_number

    def drop_connection(self, device_number, port):
        # closes the port on device
        self.network[device_number].drop(port)

    def do_things(self):
        # does the things
        # for item in self.network:
        pass

    def is_connected_to_root(self, device_number):
        # checks if device number is connected to root device
        self.network[device_number].is_connected(device_number, self.root_number)

class Device:

    def __init__(self, endpoint, port, own_number):
        # commutator is performed as list of tuples (endpoint, port used)
        self.data = [(endpoint, port)]
        self.number = own_number
        self.is_root = False

    def append(self, endpoint, port):
        if all(item[0] != endpoint for item in self.data) and all(item[1] != port for item in self.data):
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

    def get_port_by_endpoint(self, endpoint):
        for item in self.data:
            if item[0] == endpoint:
                return item[1]

    def get_endpoint_by_port(self, port):
        for item in self.data:
            if item[1] == port:
                return item[0]

    def drop(self, port):
        # closes the port given
        endpoint = self.get_endpoint_by_port(port)
        self.data.remove((endpoint, port))
