from node import Node


class Problem:

    def __init__(self, origin, destiny):
        self.origin = Node(origin, 0, Node.INITIAL, None)
        self.destiny = destiny

    def check_objective(self, node):
        return self.destiny == node.city
