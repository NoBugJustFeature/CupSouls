import arcade

from game_window import GameWindow
from variables import FPS, WIDTH, HEIGHT


def main():
    GameWindow(WIDTH, HEIGHT, 'CupSouls', FPS=FPS)
    arcade.run()


if __name__ == '__main__':
    main()