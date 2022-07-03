import requests
from ballot import Ballot
import json


class Api:
    def create_new_game(self):

        body = {
            "status_game": "ON",
            "letters_b": None,
            "letters_i": None,
            "letters_n": None,
            "letters_g": None,
            "letters_o": None,
            "winner": None,
        }

        response = requests.post("http://127.0.0.1:8000/api/v1/bingo/", data=body)
        self.validate_status(response.status_code, "The game was created successful")

    def update_game_end(self):

        response = requests.put("http://127.0.0.1:8000/api/v1/bingo/end")
        self.validate_status(response.status_code, "The game was end successful")

    def save_ball_game(self, ballot: Ballot):

        body = {"letter": ballot.letter, "number": ballot.number}

        response = requests.put(
            "http://127.0.0.1:8000/api/v1/bingo/agregar/balota", data=body
        )
        self.validate_status(response.status_code, "The ball was saved successful")

    def validate_status(self, stat, success):

        status = int(stat)

        if status >= 200 and status <= 299:
            print(success)

        elif status == "404" or status:
            print("ERROR - 404 Not Found")
