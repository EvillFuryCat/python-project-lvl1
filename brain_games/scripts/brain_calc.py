#!/usr/bin/env python
from brain_games.engine.engine import start_game
from brain_games.games import calc_game


def main():
    start_game(calc_game)


if __name__ == "__main__":
    main()
