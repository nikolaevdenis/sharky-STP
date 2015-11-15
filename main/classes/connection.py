class Connection:
    """
    stores info about connections:
    - own number of commutator (self.number)
    - number of connected commutator (self.connected_to)
    - port of connection (self.port)
    - if the connection is a 'root' connection (self.flag)
    """
    def __init__(self, self_number, connected_to, port):
        # create structure
        self.number = self_number
        self.connected_to = connected_to
        self.port = port
        self.flag = False

    def __str__(self):
        return 'Commutator #' + str(self.number) + ' is connected to #' + str(self.connected_to) + ' over port #' + self.port

    def get_connected_to(self):
        return self.connected_to
    
    def get_port(self):
        return self.port

    def is_connected_to(self, target):
        # checks if this connection connects device to target device
        if self.connected_to == target:
            return True
        else:
            return False

    def is_flagged(self):
        return self.flag

    def set_flag(self):
        self.flag = True