from node import Node
from solution import Solution


class WidthSearch:
    def __init__(self, problem):
        self.problem = problem
        self.explored = []

    def initialize_border(self):
        return self.problem.origin.children()

    def explore_node(self, node):
        node.state = Node.EXPLORED
        self.explored.append(node)

    def run(self):
        self.explored = []
        border = self.initialize_border()

        while True:
            if not border:
                return Solution(None)

            node = border.pop(0)
            self.explore_node(node)

            if self.problem.check_objective(node):
                return Solution(node)

            border += [child for child in node.children() if child not in self.explored + border]
