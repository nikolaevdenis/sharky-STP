from connection import Connection

class Node:

    def __init__(self, self_number, connected_to = None, port = None, root_flag = False):
        # commutator is performed as list of tuples (endpoint, port used)
        # # print("Creating device " + str(own_number) + " with following parameters: ")
        # # print(endpoint, port, root_flag)
        self.self_number = self_number
        self.is_root = root_flag
        if connected_to and port:
            self.connections = [Connection(self_number, connected_to, port)]
        else:
            self.connections = []
        # # print("this device has connections: " + str(self.data))

    def __str__(self):
        in_string = 'Commutator #' + str(self.self_number) + '\n'
        for connection in self.connections:
            in_string += '\troutes to #' + connection.get_connected_to() + \
                         '\tover port #' + connection.get_port() + '\n'
        if self.is_root:
            in_string += '\t----ROOT----\n'
        return in_string

    def append(self, connected_to, port):
        # if connection is unique - add
        if not self.is_connected_to(connected_to) and not self.has_port(port) and self.self_number != connected_to:
            self.connections.append(Connection(self.self_number, connected_to, port))

    def get_all_connection_targets(self):
        # returns all connected nodes as destination node numbers
        connections = []
        for connection in self.connections:
            connections.append(connection.get_connected_to())
        if connections != []:
            return connections
        else:
            return False

    def is_connected_to(self, target):
        # checks if the current commutator is connected to target one

        for connection in self.connections:
            if connection.get_connected_to() == target:
                return True
        else:
            return False

    def get_self_number(self):
        return self.self_number

    def set_root(self):
        self.is_root = True
        self.connections = []

    def get_port_by_endpoint(self, endpoint):
        # TODO - delete
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
