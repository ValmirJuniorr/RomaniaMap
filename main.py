import data.cities_graph as cities
from problem import Problem
from width_search import WidthSearch
from parse_arguments import get_arguments


def main():
    arguments = get_arguments()

    search = WidthSearch(Problem(arguments['origin'], cities.BUCHAREST))

    solution = search.run()

    solution.print()


main()
