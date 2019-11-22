from django.urls import path
from .views import *

urlpatterns = [
    path('bingo/', game_list),
    path('bingo/end', game_end),
    path('bingo/agregar/balota', save_ball_game),
    path('bingo/set/winner', set_winner)
]