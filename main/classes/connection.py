class Connection:
    """

    """
    def __init__(self, self_number, connected_to, port):
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
        if self.connected_to == target:
            return True
        else:
            return False

    def is_flagged(self):
        return self.flag

    def set_flag(self):
        self.flag = True