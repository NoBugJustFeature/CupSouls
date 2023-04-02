import arcade

from objects.player import Player
from objects.enemy import Enemy

from objects.utils.fight import fight

import random


class GameView(arcade.View):
    def __init__(self, 
                width: int = 800, 
                height: int = 600):

        super().__init__()
        self.width = width
        self.height = height

        self.background = arcade.load_texture("sprites/background/Forest/Image without mist.png")

        self.setup()


    def setup(self):
        self.player = Player("adventurer")

        self.enemies = [Enemy((random.choice([*list(range(-150, 0, 50)), *list(range(self.width, self.width+150, 50))]), 190)) for i in range(1)]


    """
    Updating the keys
    """
    def on_key_press(self, symbol: int, modifiers: int):
        self.player.move_key_press(symbol=symbol)


    def on_key_release(self, symbol: int, modifiers: int):
        self.player.move_key_release(symbol=symbol)


    """
    Updating
    """
    def on_update(self, delta_time: float):
        self.player.update(delta_time=delta_time)

        for enemy in self.enemies:
            enemy.update(delta_time=delta_time, player_x_cord=self.player.pl_sprites.center_x)

        fight(self.player, self.enemies)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.width/2, self.height/2, width=self.width, height=self.height, texture=self.background)
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()