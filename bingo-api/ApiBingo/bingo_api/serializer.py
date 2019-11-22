

from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'status_game', 'letters_b', 'letters_i', 'letters_n', 'letters_g', 'letters_o', 'winner')

