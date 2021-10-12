import shutil
import requests
from loguru import logger
import os
from models.movies import Movies
from dataclasses import dataclass
from PIL import Image
from utils.validate_data import ValidateData


@dataclass
class Search:
    title: str
    info: str = "all"
    rating: int = None

    def create_movie():
        Movies().create()
        logger.info("Movie added to the database")

    def make_movie_list(self, movies_list):
        for count, movie in enumerate(movies_list):
            print(count, movie.title)

    def select_movie_from_list(self, movies_list):
        is_this = None
        while not is_this:
            os.system("clear")
            self.make_movie_list(movies_list)

            want_image = input("Do you want to see the movie's image? (y/n)")
            if want_image.lower() == "n":
                choice = int(input("Enter the number of the movie "))
                if choice < 0 or choice > len(movies_list):
                    raise ValueError
                self.create_movie(movies_list[choice])
            else:
                index = int(input("Enter the number of the movie you want to see: "))
                movie = movies_list[index]
                self.open_movie_image(movie.image_url)
                is_this = input("Is this the movie you want? (y/n)")
                if is_this.lower() == "n":
                    is_this = False
                elif is_this.lower() == "y":
                    self.create_movie(movies_list[choice])
                    os.system("clear")
                    break

    def open_movie_image(self, image_url):
        response = requests.get(image_url, stream=True)
        with open("image/img.png", "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        with Image.open("image/img.png") as image:
            image.show()

    def _make_request(self):
        headres = {
            "X-RapidAPI-Host": "imdb8.p.rapidapi.com",
            "X-RapidAPI-Key": "061c1a3730msh2a764b091310c4dp10b4aejsn1a974600f73d",
        }
        url = "https://imdb8.p.rapidapi.com/title/find"
        params = {"q": f"{self.title}"}
        response = requests.get(str(url), headers=headres, params=params)
        return response

    def _make_response(self, response):

        # image = response.json()["results"][0]["image"]["url"]

        results = response.json()["results"]
        movies_list = []
        title_list = []
        for result in results:
            if not ValidateData().validate_data(result):
                continue
            title = result["title"]
            movie = Movies(
                id=result["id"],
                title=title,
                year=result["year"],
                image=result["image"],
                rating=self.rating,
            )
            movies_list.append(movie)
            title_list.append(title)
        self.select_movie_from_list(movies_list)

    def processor(self):
        response = self._make_request()
        self._make_response(response)


if __name__ == "__main__":
    search = Search("Harry Potter").processor()
