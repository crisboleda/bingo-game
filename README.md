
# Bingo Game

![Tests](https://github.com/crisboleda/Game-Bingo/actions/workflows/testing-action.yml/badge.svg?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## About this project
Bingo is a game of chance in which players have a card with numbers on it. As the numbers are drawn, the participants complete their cards: the first to do so is the winner.

This project uses a desktop application made with Pygame that allows the generation of ballots. It also has an API made in Django that allows you to save the data generated in each game.

### How to use:

```
1. Clone repository
2. python -m venv env
3. source env/bin/active
4. pip install requirements.txt
5. python manage.py makemigrations
6. python manage.py migrate
7. python bingo-api/ApiBingo/manage.py runserver
8. python ./Project-Bingo/start.py
```

### Things that were implemented:

- Pygame
- Multi-Theading
- CI - GitHub Actions
- Testing
- Code style