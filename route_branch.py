class RouteBranch:

    def __init__(self):
        self.string = ''

    def append_new_route_segment(self, segment):
        self.string = '{}/{}'.format(self.string, segment)
