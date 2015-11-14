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

    def get_all_ports(self):
        ports = []
        for connection in self.connections:
            ports.append(connection.get_port())
        if ports != []:
            return ports
        else:
            return False

    def is_connected_to(self, target):
        # checks if the current commutator is connected to target one

        for connection in self.connections:
            if connection.get_connected_to() == target:
                return connection.get_port()
        else:
            return False

    def get_self_number(self):
        return self.self_number

    def set_root(self):
        self.is_root = True
        self.connections = []

    def drop_by_port(self, port):
        for connection in self.connections:
            if connection.get_port() == port
                self.connections.remove(connection)
                return True
        return False

    def drop_by_target(self, target):
        for connection in self.connections:
            if connection.get_connected_to() == target
                self.connections.remove(connection)
                return True
        return False

    def flag_connection(self, port):
        for connection in self.connections:
            if connection.get_port() == port:
                connection.set_flag()

    def drop_non_root_ports(self):
        for connection in self.connections:
            if not connection.is_flagged():
                self.drop_by_port(connection.get_port())