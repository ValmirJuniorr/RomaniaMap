class Solution:
    def __init__(self, node):
        self.node = node

    def fail(self):
        return not self.node

    def steps(self):
        node = self.node
        steps = []

        while node:
            steps.append(node)
            node = node.father

        return list(reversed(steps))

    def print(self, print_with_heuristic):
        if self.fail():
            print('Não foi encontrado uma solução')

        steps = self.steps()

        for i, node in enumerate(steps):
            print('--------------------------------------------------------')
            if print_with_heuristic:
                print('{}:'.format(i), node.city, '| custo total: {} | heuristica: {}'.format(node.total_cost(), node.heuristic_value))
            else:
                print('{}:'.format(i), node.city, '| custo total: {}'.format(node.total_cost()))
            print('--------------------------------------------------------')

