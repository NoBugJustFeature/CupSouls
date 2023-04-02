import arcade

from objects.player import Player
from objects.enemy import Enemy

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

        self.enemies = [Enemy((random.choice([*list(range(-150, 0, 50)), *list(range(self.width, self.width+150, 50))]), 190)) 
                        for i in range(1)]


    """
    Updating the keys
    """
    def on_key_press(self, symbol: int, modifiers: int):
        self.player.move_key_press(symbol=symbol)


    def on_key_release(self, symbol: int, modifiers: int):
        self.player.move_key_release(symbol=symbol)


    """
    Misc
    """
    def del_enemy(self, enemy: Enemy):
        if enemy.en_sprites.cur_texture_index == len(enemy.en_sprites.death_left_textures)-1:
            self.enemies.remove(enemy)
            for i in range(2):
                self.enemies.append(Enemy((random.choice([*list(range(-150, 0, 50)), *list(range(self.width, self.width+150, 50))]), 190)))


    def death(self):
        if self.player.hp <=0:
            print("pl death")
        for enemy in self.enemies:
            if enemy.hp <=0:
                enemy.en_sprites.state_death = True
                

    def fight(self, enemy: Enemy):
        if abs(self.player.pl_sprites.center_x - enemy.en_sprites.center_x) <= 100:
            if self.player.state_attack and not enemy.en_sprites.state_hurt:
                enemy.hurt(self.player.damage)
            if enemy.state_attack and not self.player.pl_sprites.state_hurt and not self.player.damage_resistance:
                self.player.hurt(enemy.damage)

            self.death()


    """
    Updating
    """
    def on_update(self, delta_time: float):
        self.player.update(delta_time=delta_time)

        for enemy in self.enemies:
            enemy.update(delta_time=delta_time, player_x_cord=self.player.pl_sprites.center_x)
            self.del_enemy(enemy) if enemy.en_sprites.state_death == True else self.fight(enemy)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.width/2, self.height/2, width=self.width, height=self.height, texture=self.background)
        for enemy in self.enemies:
            enemy.draw()
        self.player.draw()