from .node import Node
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

    def is_connected_to_root(self, self_number):
        # checks if device number is connected to root device
        return self.network[self_number].is_connected_to(self.root_number)

    def dijkstra(self, start_node_number, end_node_number):

        # Starting Djikstra
        depth_level = 0
        node_list = []
        path_list = []
        for device in self.network:
            # creating node values and empty path
            node_list.append(10000)
            path_list.append('')
        node_list[start_node_number] = 0 # the first node has 0 value

        while 1:
            must_break = False # if should break later
            for node_number, node_value in enumerate(node_list): # looping in nodes
                if node_value == depth_level: # working only in current depth

                    if node_number != end_node_number: # if the path is found
                        current_device = self.network[node_number]
                        current_device_connections = current_device.get_all_connection_targets()

                        # for every connection target on current device
                        for current_connection in current_device_connections:
                            if node_list[current_connection] >= 1 + node_value: # Djikstra
                                node_list[current_connection] = node_value + 1
                                path_list[current_connection] = node_number

                            # drop connections to current device not to go back
                            self.network[current_connection].drop_by_target(node_number)
                    else:
                        must_break = True
                if must_break:
                    break
            if must_break:
                break
            depth_level += 1

        # flagging root connections
        current_path_point = end_node_number
        while current_path_point != start_node_number:
            # print ('Current device number = ', connection, 'Previous = ', path_list[connection])
            previous_device = path_list[current_path_point]
            if previous_device != '':
                # print ('Path point: ' + str(current_path_point))
                # root_port = self.network[previous_device].get_port_by_endpoint(self.network[connection])
                # self.network[previous_device].flag_port(root_port)
                # print ('DROPPING PORTS FOR DEVICE #' + str(previous_device))
                # self.network[previous_device].drop_non_root_ports()
                self.network[previous_device].flag_connection_by_target(current_path_point)
                current_path_point = previous_device
            else:
                break
        # # print ('Path', depth_level)

    def STP(self, root_number):
        self.network[root_number].set_root()
        for device_number, device in enumerate(self.network):
            # # print("################## NEW STP ITERATION, DEVICE NUMBER == " + str(device_number))
            self.dijkstra(device_number, root_number)
        # for device in self.network:
        #     device.drop_non_root_ports()
        for node in self.network:
            node.drop_non_root_ports()