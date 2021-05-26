from data.cities_graph import graph


class Node:
    INITIAL = 'INITIAL'
    CREATED = 'CREATED'
    EXPLORED = 'EXPLORED'

    def __init__(self, city, cost, state, father):
        self.city = city
        self.cost = cost
        self.state = state
        self.father = father

    def total_cost(self):
        father_cost = self.father.total_cost() if self.father else 0

        return self.cost + father_cost

    def children(self, state=CREATED):
        return [
            Node(*city, state, self) for city in graph[self.city]
        ]
