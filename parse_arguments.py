import argparse
import data.cities_graph as cities


STAR_ALGORITHM = 'estrela'
WIDTH_ALGORITHM = 'largura'

ALGORITHMS = [
    STAR_ALGORITHM,
    WIDTH_ALGORITHM,
]

def prepare_parse():
    description = 'You could specify the origin city for this search.\n'

    # Initialize parser
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-o", "--origin", help="Origin city")

    parser.add_argument("-a", "--algorithm", help="Algorithm that will be used in the search")

    return parser


def get_arguments():
    parser = prepare_parse()
    args = parser.parse_args()

    cities_names = cities.graph.keys()

    origin = args.origin if args.origin else cities.ARAD
    algorithm = args.algorithm.lower() if args.algorithm else STAR_ALGORITHM

    if origin not in cities_names:
        raise ValueError('{} is an invalid value for origin city param, it must be one of this values: {}'
                         .format(origin, cities_names))

    if algorithm not in ALGORITHMS:
        raise ValueError('{} is an invalid value for algorithm param, it must be one of this values: {}'
                         .format(algorithm, ALGORITHMS))

    return {
        'origin': origin,
        'algorithm': algorithm,
    }
