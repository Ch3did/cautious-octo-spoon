import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--movie",
    "-m",
    help="defines movie search",
    required=False,
)
parser.add_argument(
    "--cast",
    "-c",
    help="defines cast search",
    required=False,
)
parser.add_argument(
    "--rating",
    "-r",
    help="defines director search",
    required=False,
)
parser.add_argument(
    "--verbose",
    "-v",
    dest="verbose",
    action="store_true",
    help="set image view",
)
parser.add_argument("--no-verbose", dest="verbose", action="store_false")

parser.set_defaults(verbose=False)


def get_args():
    return parser.parse_args()
