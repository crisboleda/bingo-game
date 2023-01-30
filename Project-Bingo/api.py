import requests
import logging

from ballot import Ballot
from constants import API_URL


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

        response = requests.post(f"{API_URL}/api/v1/bingo/", data=body)
        if response.status_code == 201:
            logging.info("The game was created successful")

    def update_game_end(self):

        response = requests.put(f"{API_URL}/api/v1/bingo/end")
        if response.status_code == 200:
            logging.info("The game was finished successful")

    def save_ball_game(self, ballot: Ballot):
        """
        Save a ballot
        """

        body = {"letter": ballot.letter, "number": ballot.number}

        response = requests.put(f"{API_URL}/api/v1/bingo/agregar/balota", data=body)
        if response.status_code == 201:
            logging.info("The ballot was saved successful")
