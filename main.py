import data.cities_graph as cities
from parse_arguments import get_arguments, STAR_ALGORITHM
from problem import Problem
from star_search import StarSearch
from width_search import WidthSearch


def main():
    arguments = get_arguments()
    algorithm = arguments['algorithm']
    origin = arguments['origin']

    if algorithm == STAR_ALGORITHM:
        search = StarSearch(Problem(origin, cities.BUCHAREST))
    else:
        search = WidthSearch(Problem(origin, cities.BUCHAREST))

    solution = search.run()

    solution.print(print_with_heuristic=algorithm == STAR_ALGORITHM)


main()
