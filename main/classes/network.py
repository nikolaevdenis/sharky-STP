from node import Node
from random import randint

class Network:

    def __init__(self, max):
        # creates random network
        self.network = []
        self.root_number = None
        for node in range(max):
            self.network.append(Node(node))
            for j in range(max):
                target = randint(0, max-1)
                if target != node:
                    self.network[node].append(randint(0, max-1), randint(0, max-1))

    def __str__(self):
        in_string = ''
        for node in self.network:
            in_string += str(node) + '\n'
        return in_string

    def is_connected(self, self_number, target):
        # checks if the startpoint commutator is connected to endpoint
        # if yes, returns a connection port
        # if no, returns False
        return self.network[self_number].is_connected_to(target)

    def tag_root(self, self_number):
        # tags the device as root, remember the root device number
        self.network[self_number].set_root()
        self.root_number = self_number

    def drop_connection(self, self_number, port):
        # closes the port on device
        self.network[self_number].drop_by_port(port)

    def do_things(self):
        # does the things
        for i in range(len(self.network)):
            if self.is_connected_to_root(i) == False:
                del self.network[i]
            else:
                for port in self.network[i].get_all_ports():
                    if self.network[i].get_endpoint_by_port(port) != self.root_number:
                        self.network[i].drop(port)

    def is_connected_to_root(self, self_number):
        # checks if device number is connected to root device
        return self.network[self_number].is_connected_to(self.root_number)

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
