"""
classes file implies all classes, which will be used in current program
"""
from random import randint

class Network:

    def __init__(self, max):
        # creates random network
        self.network = []
        self.root_number = None
        for i in range(max):
            self.network.append(Device(i))
            for j in range(max):
                target = randint(0, max-1)
                if target != i:
                    self.network[i].append(randint(0, max-1), randint(0, max-1), False)
        # self.network.append(Device(1, 1, 0, False))
        # self.network[0].append(2, 2, False)
        # self.network[0].append(3, 3, False)
        # self.network.append(Device(0, 0, 1, False))
        # self.network.append(Device(0, 0, 2, False))
        # self.network.append(Device(0, 0, 3, False))
        # self.network.append(Device(3, 0, 4, False))
        # self.network[3].append(4, 4, False)
        self.reference_network = self.network[:]

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
        # print ('Starting djikstra for ', startpoint, 'to', endpoint)
        start_device = network[startpoint]

        node_list = []
        path_list = []
        for device in network:
            # set incredibly length!
            node_list.append(10000)
            path_list.append('')

        node_list[startpoint] = 0
        device_number = startpoint
        depth_level = 0
        connection = 0
        last_depth = 0
        while 1:
            must_break = False
            for device_number, value in enumerate(node_list):
                if value == depth_level:
                    if device_number != endpoint:
                        # print ('Current device_number', device_number)
                        if node_list[device_number] == depth_level:
                            current_device = network[device_number]
                            current_device_connections = current_device.get_connections()
                            # # print('current_device', str(device_number), 'current_device_connections', str(current_device_connections))
                            for connection in current_device_connections:
                                if node_list[connection] >= 1 + node_list[device_number]:
                                    # print ('Found a close one', connection)
                                    node_list[connection] = node_list[device_number] + 1
                                    path_list[connection] = device_number
                                    last_depth = node_list[connection]
                                # drop connections to current device not to go back
                                # first, get the object of connected device
                                connected_device_port = network[connection].get_port_by_endpoint(device_number)
                                # drop connection to connected device
                                # # print ('Backwards Connection', connection, 'Connected device port', connected_device_port)
                                if connected_device_port:
                                    network[connection].drop(connected_device_port)
                                # # print (str(network[device_number]))
                    else:
                        must_break = True
                if must_break:
                    break
            if must_break:
                break
            depth_level = last_depth
        connection = endpoint

        while connection != startpoint:
            # # print ('Current device number = ', connection, 'Previous = ', path_list[connection])
            previous_device = path_list[connection]
            if previous_device != '':
                # root_port = self.network[previous_device].get_port_by_endpoint(self.network[connection])
                # self.network[previous_device].flag_port(root_port)
                # print ('DROPPING PORTS FOR DEVICE #' + str(previous_device))
                # self.network[previous_device].drop_non_root_ports()
                self.network[previous_device].drop_all_by_endpoint(connection)
                connection = previous_device
            else:
                break
        # # print ('Path', depth_level)

    def STP(self, root):
        self.network[root].set_root()
        for device_number, device in enumerate(self.network):
            # # print("################## NEW STP ITERATION, DEVICE NUMBER == " + str(device_number))
            self.dijkstra(device_number, root)
        # for device in self.network:
        #     device.drop_non_root_ports()


class Device:

    def __init__(self, own_number, endpoint = None, port = None, root_flag = False):
        # commutator is performed as list of tuples (endpoint, port used)
        # # print("Creating device " + str(own_number) + " with following parameters: ")
        # # print(endpoint, port, root_flag)
        if endpoint and port:
            self.data = [[endpoint, port, root_flag]]
        else:
            self.data = []
        # # print("this device has connections: " + str(self.data))
        self.number = own_number
        self.is_root = False

    def append(self, endpoint, port, root_flag):
        # if connection is unique - add
        if all(item[0] != endpoint for item in self.data) and all(item[1] != port for item in self.data) and endpoint != self.number:
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
        self.data = []

    def get_port_by_endpoint(self, endpoint):
        for item in self.data:
            if item[0] == endpoint:
                return item[1]
        return False

    def get_endpoint_by_port(self, port):
        for item in self.data:
            if item[1] == port:
                return item[0]

    def get_all_ports(self):
        return [item[1] for item in self.data]

    def drop(self, port, endpoint = False):
        # closes the port given
        if not endpoint:
            endpoint = self.get_endpoint_by_port(port)
        # # print ('Kill connection on device #', self.number, 'endpoint:', endpoint, 'port', port)
        self.data.remove([endpoint, port, False])
        # try:
        #     endpoint = self.get_endpoint_by_port(port)
        #     self.data.remove([endpoint, port, False])
        # except:
        #     # print ('Cannot drop port #', port, 'on device #', self.number)
    def drop_all_by_endpoint(self, endpoint):
        while len(self.data) > 1:
            for item in self.data:
                if item[0] != endpoint:
                    # print ('Dropping ' + str(item))
                    self.drop(item[1], item[0])

    def flag_port(self, port):
        for item in self.data:
            if item[1] == port:
                item[2] = True
                break

    def drop_non_root_ports(self):
        for item in self.data:
            if not item[2]:
                # print ('On device ' + str(self.number) + ' Dropping port ' + str(item[1]) + ' Routing to ' + str(item[0]) + ' ' + str(item[2]))
                self.drop(item[1])
