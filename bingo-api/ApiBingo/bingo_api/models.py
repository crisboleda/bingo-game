from django.db import models


class Game(models.Model):

    data_game = models.DateField(auto_now=True)
    status_game = models.CharField(max_length=5, null=False)

    letters_b = models.CharField(max_length=100, null=True)
    letters_i = models.CharField(max_length=100, null=True)
    letters_n = models.CharField(max_length=100, null=True)
    letters_g = models.CharField(max_length=100, null=True)
    letters_o = models.CharField(max_length=100, null=True)

    winner = models.CharField(max_length=50, null=True)
