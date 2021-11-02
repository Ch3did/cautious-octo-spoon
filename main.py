from models.search import Search
from utils.args import get_args

args = get_args()


if args.movie:
    search = Search(title=args.movie, rating=args.rating)
    if args.verbose:
        search.verbose = True
    search.processor()

if args.cast:
    print("Feature not ready yet")


# TODO: Make a Search for movies already classified
# TODO: Make a fields search
