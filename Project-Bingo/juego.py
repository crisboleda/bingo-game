from email.mime import image
import pygame
from pygame.locals import *
import sys
from datetime import datetime
import threading
import time

from bola import Bola


class Juego:
    def __init__(self, logic, api, seconds_delay):
        self.screen = pygame.display.set_mode((500, 400))
        self.api = api
        self.logic = logic
        self.text_ball = None
        self.is_pause = True
        self.seconds_delay = seconds_delay

    def generate_ball_worker(self, arg):
        while not arg["stop"]:
            time.sleep(self.seconds_delay)
            if not self.is_pause:
                bola = self.logic.generar_bola()
                self.api.save_ball_game(bola)
                self.text_ball = self.render_text(
                    bola.visualizar_bola(), (255, 255, 255), 90
                )

    def render_text(self, string, color, size):
        font = pygame.font.SysFont("arial", size)
        return font.render(string, True, color)

    def start_game(self):
        bola = Bola("b", 0)
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
            self.screen.blit(balota, (210, 65))

            if len(bola.visualizar_bola()) == 2:
                self.screen.blit(self.text_ball, (280, 130))
            else:
                self.screen.blit(self.text_ball, (255, 133))

            self.screen.blit(title_game, (145, 5))
            self.screen.blit(remenber, (10, 370))

            text_time = self.render_text(self.get_time_now(), (60, 60, 60), 15)
            self.screen.blit(text_time, (345, 373))

            pygame.display.flip()
            pygame.display.update()

    def get_time_now(self):
        return str(datetime.now())

    def get_image_play_or_pause_button(self):
        image_url = "img/play-button.png" if self.is_pause else "img/pause-button.png"
        return pygame.image.load(image_url)
