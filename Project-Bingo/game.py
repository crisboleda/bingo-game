import pygame
from pygame.locals import *
import sys
from datetime import datetime
import threading
import time

from constants import COORDINATE_IMAGE_BALLOT_X, COORDINATE_IMAGE_BALLOT_Y, MODE_TESTING


class Game:
    def __init__(self, logic, api, seconds_delay, mode=None):
        self.api = api
        self.logic = logic
        self.text_ball = None
        self.is_pause = True
        self.seconds_delay = seconds_delay
        self.mode = mode

    def generate_ball_worker(self, arg):
        while not arg["stop"]:
            time.sleep(self.seconds_delay)
            if not self.is_pause:
                ballot = self.logic.generate_ballot()
                self.api.save_ball_game(ballot)
                self.text_ball = self.render_text(
                    ballot.show_ballot(), (255, 255, 255), 90
                )

    def render_text(self, string, color, size):
        font = pygame.font.SysFont("arial", size)
        return font.render(string, True, color)

    def start_game(self):
        self.screen = pygame.display.set_mode((500, 400))
        pygame.init()
        self.api.create_new_game()

        self.text_ball = self.render_text("???", (255, 255, 255), 90)
        title_game = self.render_text("¡Super Bingo!", (50, 50, 50), 35)
        remenber = self.render_text(
            "Recuerde gritar 'Bingo' - Suerte :D", (125, 125, 125), 19
        )

        pygame.display.set_caption("Bingo")
        button_image = self.get_image_play_or_pause_button()
        balota = pygame.image.load("img/balota.png")

        info = {"stop": False}
        thread = threading.Thread(target=self.generate_ball_worker, args=(info,))
        thread.start()

        while True:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    info["stop"] = True
                    thread.join()
                    self.api.update_game_end()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    x_mouse, y_mouse = pygame.mouse.get_pos()

                    if (
                        x_mouse >= 60
                        and x_mouse <= 188
                        and y_mouse >= 110
                        and y_mouse <= 238
                    ):
                        self.is_pause = not self.is_pause
                        button_image = self.get_image_play_or_pause_button()

            self.screen.blit(button_image, (60, 125))
            self.screen.blit(
                balota, (COORDINATE_IMAGE_BALLOT_X, COORDINATE_IMAGE_BALLOT_Y)
            )

            ballot_text_coordinate_x = self.__get_coordinates_ballot_text_inside_parent(
                COORDINATE_IMAGE_BALLOT_X,
                balota.get_rect().centerx,
                self.text_ball.get_rect().centerx,
            )
            ballot_text_coordinate_y = self.__get_coordinates_ballot_text_inside_parent(
                COORDINATE_IMAGE_BALLOT_Y,
                balota.get_rect().centery,
                self.text_ball.get_rect().centery,
            )

            self.screen.blit(
                self.text_ball, (ballot_text_coordinate_x, ballot_text_coordinate_y)
            )

            self.screen.blit(title_game, (145, 5))
            self.screen.blit(remenber, (10, 370))

            text_time = self.render_text(self.get_time_now(), (60, 60, 60), 15)
            self.screen.blit(text_time, (345, 373))

            pygame.display.flip()
            pygame.display.update()

            if self.mode == MODE_TESTING:
                break

    def get_time_now(self):
        return str(datetime.now())

    def get_image_play_or_pause_button(self):
        image_url = "img/play-button.png" if self.is_pause else "img/pause-button.png"
        return pygame.image.load(image_url)

    def __get_coordinates_ballot_text_inside_parent(
        self, coordinate_parent: int, middle_parent: int, middle_child: int
    ):
        return coordinate_parent + middle_parent - middle_child
