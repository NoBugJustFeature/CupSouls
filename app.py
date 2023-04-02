import arcade

from views.start_view import StartView
from variables import FPS, WIDTH, HEIGHT


def main():
    window = arcade.Window(width=WIDTH, 
                           height=HEIGHT, 
                           title='CupSouls', 
                           update_rate=1/FPS)
    
    start_view = StartView(width=WIDTH,
                           height=HEIGHT)
    
    window.show_view(start_view)
    arcade.run()


if __name__ == '__main__':
    main()