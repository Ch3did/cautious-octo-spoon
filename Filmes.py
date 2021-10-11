import requests
from pprint import pprint 
from dataclasses import dataclass


@dataclass
class  Films:
    title: str
    request_info: str = "all"


    def _make_request(self):
        headres = {
            "X-RapidAPI-Host" : "imdb8.p.rapidapi.com",
            "X-RapidAPI-Key" : "061c1a3730msh2a764b091310c4dp10b4aejsn1a974600f73d"
        }
        url = 'https://imdb8.p.rapidapi.com/title/find'
        params = {
            "q": f"{self.title}"
        }
        response = requests.get(str(url), headers=headres, params=params)
        
        for results in response.json()["results"]:
            with open(f"response.json", "w") as file:
                file.write(response.text)
        
        
        pprint(response.json()["results"][0])

        #     pprint(response.json())

    def _make_response(self, request_info):
        pass

if __name__ == "__main__":
    Films(title="game of thrones")._make_request()