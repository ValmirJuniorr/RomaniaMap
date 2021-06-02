from data.cities_graph import graph, heuristic_values


class Node:
    def __init__(self, city, cost, father, heuristic_value):
        self.city = city
        self.cost = cost
        self.father = father
        self.heuristic_value = heuristic_value

    def total_cost(self):
        father_cost = self.father.total_cost() if self.father else 0

        return self.cost + father_cost

    def children(self):
        return [
            Node(*city, self, heuristic_values[city[0]]) for city in graph[self.city]
        ]
