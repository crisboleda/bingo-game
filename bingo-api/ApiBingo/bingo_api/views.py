from django.shortcuts import render

#Import from rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Import my app
from .models import Game
from .serializer import GameSerializer
from .logic.save import SaveBall


@api_view(['GET', 'POST', 'PUT'])
def game_list(request):

    if request.method == 'GET':
        queryset = Game.objects.filter(status_game='ON')
        serializer = GameSerializer(queryset, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response({"response": "status: 201  - The game started successful"})
        return Response({"response": "ERROR"})


@api_view(['PUT'])
def game_end(request):

    if request.method == 'PUT':
        
        try:
            obj = Game.objects.get(status_game='ON')
            obj.status_game = 'OFF'
            obj.save()

            return Response({"response": "Ended successful"})

        except Game.DoesNotExist:
            return Response({"response": "404 - Game Not Found"})


@api_view(['PUT'])
def save_ball_game(request):
    
    if request.method == 'PUT':
        save = SaveBall()

        try:
            obj = Game.objects.get(status_game='ON')
            letter = request.data['letter']
            number = request.data['number']

            result = save.add_ball(letter, number)

            return Response({"response:": result})

        except Game.DoesNotExist:
            return Response({'response': "404 - Game Not Found"})


@api_view(['PUT'])
def set_winner(request):

    if request.method == 'PUT':

        try:
            game = Game.objects.get(status_game='ON')
            winner = request.data['winner']
            print(winner)
            game.winner = winner
            game.save()

            return Response({'response': "Winner was updated successful"})

        except Game.DoesNotExist:
            return Response({'response': "Game Not Found"})
