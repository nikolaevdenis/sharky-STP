import node

class Network:

    def __init__(self, max):
        # creates random network
        self.network = []
        self.root_number = None
        for i in range(max):
            self.network.append(Node(i))
            for j in range(max):
                target = randint(0, max-1)
                if target != i:
                    self.network[i].append(randint(0, max-1), randint(0, max-1), False)
        # self.network.append(Node(1, 1, 0, False))
        # self.network[0].append(2, 2, False)
        # self.network[0].append(3, 3, False)
        # self.network.append(Node(0, 0, 1, False))
        # self.network.append(Node(0, 0, 2, False))
        # self.network.append(Node(0, 0, 3, False))
        # self.network.append(Node(3, 0, 4, False))
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
