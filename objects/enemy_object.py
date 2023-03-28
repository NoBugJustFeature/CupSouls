from typing import Tuple
import arcade

from objects.utils.overrideSprite \
    import OverrideSprite as Sprite


class Enemy_object():
    def __init__(self, 
                coords: Tuple[float, float],
                movespeed: float,
                hp: int, 
                damage: float, 
                ):

        self.x_cord = coords[0]
        self.y_cord = coords[1]
        self.movespeed = movespeed
        self.hp = hp
        self.damage = damage

        self.en_sprites = Sprite()
        self.en_sprite_list = arcade.SpriteList()


    """
    Actions function
    """
    def action(self, pl_x):
        if pl_x-100 <= self.en_sprites.center_x <= pl_x+100:
            self.en_sprites.change_x = 0
            self.en_sprites.state_attack = True

        elif pl_x > self.en_sprites.center_x:
            self.en_sprites.change_x = self.movespeed
            self.en_sprites.state_attack = False

        elif pl_x < self.en_sprites.center_x:
            self.en_sprites.change_x = -self.movespeed
            self.en_sprites.state_attack = False


    """
    Update functions
    """
    def update(self, delta_time: float, player_x_cord):
        self.en_sprite_list.update_animation(delta_time=delta_time)
        self.action(pl_x=player_x_cord)


    def draw(self):
        self.en_sprite_list.draw()