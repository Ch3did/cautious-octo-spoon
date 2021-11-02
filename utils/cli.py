import os
import shutil
from pprint import pprint
from time import sleep

import psutil
import requests
from PIL import Image


def show_help(self):
    print(
        """
    Usage:
        ./main.py [options]
    Options:
        -h, --help: Show this help message.
        """
    )


def set_something(something):
    clear()
    pprint(something)


def get_something(output):
    clear()
    return input(output)


def select_movie_from_images(movies_list):
    for movie in movies_list:
        response = requests.get(movie["image"]["url"], stream=True)
        with open("image/img.png", "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        img = Image.open("image/img.png")
        img.show()
        sleep(2)
    return get_something("Qual o filme que irá salvar? :")


def clear():
    os.system("clear")
