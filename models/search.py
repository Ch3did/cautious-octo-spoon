from dataclasses import dataclass

import requests
from sqlalchemy.sql.expression import null

from load_env import API_KEY, API_URL
from models.movies import Movies
from utils.cli import get_something, select_movie_from_images, set_something


@dataclass
class Search:
    title: str
    info: str = "all"
    rating: int = None
    verbose: bool = False

    @staticmethod
    def make_movie_list(self, movies_list):
        for count, movie in enumerate(movies_list):
            print(count, movie.title, movie.year)

    @staticmethod
    def validate_data(result):
        if not "title" in result:
            return False
        if not "image" in result:
            return False
        if not "url" in result["image"]:
            return False
        return True

    def _make_request(self):
        headres = {
            "X-RapidAPI-Host": "imdb8.p.rapidapi.com",
            "X-RapidAPI-Key": API_KEY,
        }
        url = API_URL
        params = {"q": f"{self.title}"}
        response = requests.get(str(url), headers=headres, params=params)
        return response

    def _make_response(self, response):
        results = response.json()["results"]
        movies_list = []
        for result in results:
            if not self.validate_data(result):
                continue
            movies_list.append(
                {
                    "title": result["title"],
                    "year": result["year"],
                    "image": result["image"],
                    "rating": self.rating,
                }
            )
        set_something(movies_list)
        if self.verbose:
            index = select_movie_from_images(movies_list)
        else:
            index = get_something("Qual o indice do filme escolhido?")

        movie = Movies(
            id=None,
            title=movies_list[int(index)]["title"],
            year=movies_list[int(index)]["year"],
            image=movies_list[int(index)]["image"],
            rating=None,
        )
        movie.create()

    def processor(self):
        response = self._make_request()
        self._make_response(response)


if __name__ == "__main__":
    search = Search("Harry Potter").processor()
