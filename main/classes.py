"""
classes file implies all classes, which will be used in current program
"""
from random import randint

class Network:

    def __init__(self, max):
        # creates random network
        self.network = []
        self.root_number = None
        # for i in range(max):
        #     self.network.append(Device(0, 0, i, False))
        #     for j in range(max):
        #         self.network[i].append(randint(0, j), randint(0, j))
        self.network.append(Device(1, 1, 0, False))
        self.network[0].append(2, 2, False)
        self.network[0].append(3, 3, False)
        self.network.append(Device(0, 0, 1, False))
        self.network.append(Device(0, 0, 2, False))
        self.network.append(Device(0, 0, 3, False))


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
        for i in range(len(self.network)):
            if self.is_connected_to_root(i) == False:
                del self.network[i]
            else:
                for port in self.network[i].get_all_ports():
                    if self.network[i].get_endpoint_by_port(port) != self.root_number:
                        self.network[i].drop(port)

    def is_connected_to_root(self, device_number):
        # checks if device number is connected to root device
        self.network[device_number].is_connected(self.root_number)

    def dijkstra(self, startpoint, endpoint):

        network = self.network[:]

        start_device = network[startpoint]

        node_list = []

        for device in network:
            # set incredibly length!
            node_list.append(10000)

        node_list[startpoint] = 0

        device_number = startpoint

        while device_number != endpoint:

            current_device = network[device_number]
            current_device_connections = current_device.get_connections()
            print('current_device', str(device_number), 'current_device_connections', str(current_device_connections))
            for connection in current_device_connections:
                if node_list[connection] >= 1 + node_list[device_number]:
                    node_list[connection] = node_list[device_number] + 1

                # drop connections to current device not to go back
                # first, get the object of connected device
                connected_device_port = network[connection].get_port_by_endpoint(device_number)
                # drop connection to connected device
                print (connection, connected_device_port)
                network[connection].drop(connected_device_port)
                print (str(network[device_number]))

            device_number += 1

class Device:

    def __init__(self, endpoint, port, own_number, root_flag):
        # commutator is performed as list of tuples (endpoint, port used)
        self.data = [[endpoint, port, root_flag]]
        self.number = own_number
        self.is_root = False

    def append(self, endpoint, port, root_flag):
        if all(item[0] != endpoint for item in self.data) and all(item[1] != port for item in self.data):
            self.data.append([endpoint, port, root_flag])

    def get_connections(self):
        # returns all connected nodes as destination node numbers
        return [connection[0] for connection in self.data]

    def __str__(self):
        in_string = 'Commutator #' + str(self.number) + '\n'
        for item in self.data:
            in_string += '\troutes to #' + str(item[0]) + \
                         '\tover port #' + str(item[1]) + '\n'
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

    def get_own_number(self):
        return self.number

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

    def get_all_ports(self):
        return [item[1] for item in self.data]

    def drop(self, port):
        # closes the port given
        endpoint = self.get_endpoint_by_port(port)
        self.data.remove([endpoint, port, False])
