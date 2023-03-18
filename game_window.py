import arcade

from objects.player import Player


class GameWindow(arcade.Window):
    def __init__(self, 
                width: int = 800, 
                height: int = 600, 
                title: str = 'CupSouls', 
                fullscreen: bool = False, 
                resizable: bool = False, 
                FPS: float = 60):

        """
        Init screen
        """
        self.update_rate = 1/FPS

        super().__init__(width, height, title, fullscreen, resizable, self.update_rate)

        self.set_location(200, 50)
        self.background = arcade.load_texture("sprites/background/Forest/Image without mist.png")

        self.setup()


    def setup(self):
        self.pl = Player()


    """
    Updating the keys
    """
    def on_key_press(self, symbol: int, modifiers: int):
        self.pl.move_key_press(symbol=symbol)


    def on_key_release(self, symbol: int, modifiers: int):
        self.pl.move_key_release(symbol=symbol)       


    """
    Updating the screen
    """
    def on_update(self, delta_time: float):
        self.pl.update_animation(delta_time=delta_time)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.width/2, self.height/2, width=self.width, height=self.height, texture=self.background)
        self.pl.draw()