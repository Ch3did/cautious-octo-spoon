from models.search import Search
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

args = parser.parse_args()


if args.movie:
    Search(title=args.movie, rating=args.rating).processor()

if args.cast:
    print("Feature not ready yet")

# TODO: Make a Search for movies already classified
# TODO: Make a fields search
