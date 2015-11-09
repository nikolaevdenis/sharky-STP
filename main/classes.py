"""
classes file implies all classes, which will be used in current program
"""

class Commutator:
    def __init__(self, endpoint, port, own_number):
        # commutator is performed as dictionary in form
        # endpoint -> port
        if self.data:
            self.data.append([endpoint, port])
        else:
            self.data = [endpoint, port]
        self.own_number = own_number
    def __str__(self):
        in_string = ''
        for item in self.data:
            in_string += 'Commutator #' + str(self.own_number) \
                        + '\troutes to #' + str(item[0])\
                        + '\tthrough port #' + str(item[1]) + '\n'
        return in_string
