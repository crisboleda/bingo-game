from speaker.speaker_factory import SpeakerFactory

from generador import Generator
from logic import Logic
from constants import SPEAKER_DELAY_SECONDS, DEFAULT_SPEAKER_TYPE
from api import Api
from game import Game

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

    generator = Generator()
    speaker_factory = SpeakerFactory(speaker_name=config["speaker"])
    speaker = speaker_factory.get_speaker()

    logic = Logic(generator=generator, speaker=speaker)
    api = Api()

    game = Game(logic=logic, api=api, seconds_delay=config["delay"])
    game.start_game()
