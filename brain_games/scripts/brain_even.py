#!/usr/bin/env python
from brain_games.engine.engine import start_game
from brain_games.games import even_games


def main():
    start_game(even_games)


if __name__ == "__main__":
    main()
