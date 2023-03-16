import arcade

from objects.player import Player
from variables import FPS


class GameWindow(arcade.Window):
    def __init__(self, 
                width: int = 800, 
                height: int = 600, 
                title: str = 'CupSouls', 
                fullscreen: bool = False, 
                resizable: bool = False, 
                FPS: float = 60):

        self.update_rate = 1/FPS

        super().__init__(width, height, title, fullscreen, resizable, self.update_rate)

        self.set_location(200, 50)
        self.background = arcade.load_texture("sprites/background/Forest/Image without mist.png")

        self.pl = Player()


    def on_key_press(self, symbol: int, modifiers: int):
        self.pl.move_key_press(symbol=symbol)


    def on_key_release(self, symbol: int, modifiers: int):
        self.pl.move_key_release(symbol=symbol)       


    def on_update(self, delta_time: float):
        self.pl.update(delta_time=delta_time)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.width/2, self.height/2, width=self.width, height=self.height, texture=self.background)
        self.pl.draw()

def main():
    GameWindow(1024, 768, 'CupSouls', FPS=FPS)
    arcade.run()


if __name__ == '__main__':
    main()