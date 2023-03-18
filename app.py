import arcade

from game_window import GameWindow
from variables import FPS


def main():
    GameWindow(1024, 768, 'CupSouls', FPS=FPS)
    arcade.run()


if __name__ == '__main__':
    main()