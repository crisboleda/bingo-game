from ..models import Game


class SaveBall():

    def add_ball(self, letter, number):
        list_numbers = []

        # Valido con el catch que si exista un juego ON
        try:
            game = Game.objects.get(status_game='ON')
            letters = self.__get_numbers_letter(letter, game)

            if letters == None:
                list_numbers.append(str(number))
                self.__save_ball(letter, game, str(number))
            else:
                list_numbers = letters.split(',')
                list_numbers.append(str(number))
                self.__save_ball(letter, game, ','.join(list_numbers))

            return '201 - The ball was saved successful'

        except Game.DoesNotExist:
            return '404 - Game Not Found'


    def __save_ball(self, letter, game, data):

        if letter == "B":
            game.letters_b = data

        elif letter == "I":
            game.letters_i = data

        elif letter == "N":
            game.letters_n = data

        elif letter == "G":
            game.letters_g = data

        else:
            game.letters_o = data

        game.save()


    def __get_numbers_letter(self, letter, game):
        
        if letter == "B":
            return game.letters_b

        elif letter == "I":
            return game.letters_i

        elif letter == "N":
            return game.letters_n

        elif letter == "G":
            return game.letters_g

        return game.letters_o


    def convert_string_number(self, list_strings):
        new_list = []

        for item in list_strings:
            new_list.append(int(item))

        return new_list