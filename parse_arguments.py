import argparse
import data.cities_graph as cities


def prepare_parse():
    description = 'You could specify the origin city for this search.\n'

    # Initialize parser
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-o", "--origin", help="Origin city")

    return parser


def get_arguments():
    parser = prepare_parse()
    args = parser.parse_args()

    cities_names = cities.graph.keys()

    origin = args.origin if args.origin else cities.ARAD

    if origin not in cities_names:
        raise ValueError('origin city param must be onde of this values: {}'.format(cities_names))

    return {
        'origin': origin
    }
