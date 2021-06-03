from node import Node
from data.cities_graph import heuristic_values


class Problem:
    def __init__(self, origin, destiny):
        self.origin = Node(origin, 0, None, heuristic_values[origin])
        self.destiny = destiny

    def check_objective(self, node):
        return self.destiny == node.city
