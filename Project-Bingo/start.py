from speaker.speaker_factory import SpeakerFactory

from generador import Generador
from logic import Logic
from constants import SPEAKER_DELAY_SECONDS, DEFAULT_SPEAKER_TYPE
from api import Api
from juego import Juego

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ballot generator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-d",
        "--delay",
        type=int,
        default=SPEAKER_DELAY_SECONDS,
        help="Delay for ballot generation",
    )

    parser.add_argument(
        "-s", "--speaker", type=str, default=DEFAULT_SPEAKER_TYPE, help="Speaker type"
    )

    args = parser.parse_args()
    config = vars(args)

    generador = Generador()
    speaker_factory = SpeakerFactory(speaker_name=config["speaker"])
    speaker = speaker_factory.get_speaker()

    logic = Logic(generador=generador, speaker=speaker)
    api = Api()

    juego = Juego(logic=logic, api=api, seconds_delay=config["delay"])
    juego.start_game()
