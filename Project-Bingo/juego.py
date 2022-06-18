
import pygame
from pygame.locals import *
import sys
from os import system
from datetime import datetime

from generador import Generador
from logic import Logic
from bola import Bola
from api import Api

from speaker.speaker_factory import SpeakerFactory

class Juego():


    def __init__(self, logic, api):
        self.screen = pygame.display.set_mode((500, 400))
        self.api = api
        self.logic = logic


    def render_text(self, string, color, size):
        font = pygame.font.SysFont("arial", size)
        return font.render(string, True, color)


    def start_game(self):
        bola = Bola('b', 0)
        pygame.init()
        self.api.create_new_game()

        text_bola = self.render_text("???", (255, 255, 255), 90)
        title_game = self.render_text("¡Super Bingo!", (50, 50, 50), 35)
        remenber = self.render_text("Recuerde gritar 'Bingo' - Suerte :D", (125, 125, 125), 19)

        pygame.display.set_caption("Bingo")
        imagen = pygame.image.load("img/play-button.png")
        balota = pygame.image.load("img/balota.png")
    
        while True:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.api.update_game_end()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    x_mouse, y_mouse = pygame.mouse.get_pos()

                    if x_mouse >= 60 and x_mouse <= 188 and y_mouse >= 110 and y_mouse <= 238:
                        bola = self.logic.generar_bola()
                        self.api.save_ball_game(bola)
                        text_bola = self.render_text(bola.visualizar_bola(), (255, 255, 255), 90)
                        

            self.screen.blit(imagen, (60, 125))
            self.screen.blit(balota, (210, 65))

            if len(bola.visualizar_bola()) == 2:
                self.screen.blit(text_bola, (280, 130))
            else:
                self.screen.blit(text_bola, (255, 133))

            self.screen.blit(title_game, (145, 5))
            self.screen.blit(remenber, (10, 370))

            time = self.render_text(self.get_time_now(), (60, 60, 60), 15)
            self.screen.blit(time, (345, 373))

            pygame.display.flip()
            pygame.display.update()

    def get_time_now(self):
        return str(datetime.now())


if __name__ == '__main__':
    generador = Generador()
    speaker_factory = SpeakerFactory("GTTS")
    speaker = speaker_factory.get_speaker()

    logic = Logic(generador=generador, speaker=speaker)
    api = Api()

    juego = Juego(logic, api)
    juego.start_game()