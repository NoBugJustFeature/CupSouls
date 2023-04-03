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
                frames_befor_attack: int,
                frames_hurt: int
                ):

        self.x_cord = coords[0]
        self.y_cord = coords[1]
        self.movespeed = movespeed
        self.hp = hp
        self.damage = damage

        """
        States
        """
        self.state_attack = False
        self.damage_resistance = False

        """
        Sprites
        """
        self.frames_befor_attack = frames_befor_attack
        self.frames_hurt = frames_hurt

        self.en_sprites = Sprite()
        self.en_sprite_list = arcade.SpriteList()


    """
    Actions function
    """
    def action(self, pl_x: float):
        if not self.en_sprites.state_hurt and not self.en_sprites.state_death:
            if abs(self.en_sprites.center_x - pl_x) <= 100:
                self.en_sprites.change_x = 0
                self.en_sprites.state_attack =True

            elif pl_x > self.en_sprites.center_x:
                self.en_sprites.change_x = self.movespeed
                self.en_sprites.state_attack = False

            elif pl_x < self.en_sprites.center_x:
                self.en_sprites.change_x = -self.movespeed
                self.en_sprites.state_attack = False

            if self.en_sprites.cur_texture_index >= self.frames_befor_attack:
                self.state_attack = True
            else: 
                self.state_attack = False


    """
    Hurt
    """
    def hurt(self, damage: float):
        self.hp -= damage
        self.en_sprites.state_hurt = True
        self.damage_resistance = True

    def update_frame_hitted(self):
        if self.en_sprites.state_hurt == True:
            if self.en_sprites.cur_texture_index == self.frames_hurt-1:
                self.en_sprites.state_hurt = False

    """
    Update functions
    """
    def update(self, delta_time: float, player_x_cord: float):
        self.en_sprite_list.update_animation(delta_time=delta_time)
        self.action(pl_x=player_x_cord)
        self.update_frame_hitted()


    def draw(self):
        self.en_sprite_list.draw()