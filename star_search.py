from solution import Solution


class StarSearch:
    def __init__(self, problem):
        self.problem = problem
        self.explored = []

    def initialize_border(self):
        return self.sort_children(self.problem.origin.children())

    def explore_node(self, node):
        self.explored.append(node)

    @staticmethod
    def sort_children(children):
        return sorted(children, key=lambda node: node.total_cost() + node.heuristic_value)

    def run(self):
        self.explored = []
        border = [self.problem.origin]

        while True:
            if not border:
                return Solution(None)

            node = border.pop(0)
            self.explored.append(node)

            if self.problem.check_objective(node):
                return Solution(node)

            border += [child for child in node.children() if child not in self.explored + border]

            border = self.sort_children(border)
