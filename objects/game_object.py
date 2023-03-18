from typing import Tuple
import arcade

from objects.utils.overrideAnimatedWalkingSprite \
    import OverrideAnimatedWalkingSprite as AnimatedWalkingSprite


class Game_object():
    def __init__(self, 
                coords: Tuple[float, float],
                movespeed: float,
                hp: int, 
                damage: float, 
                armor: int, 
                cd: float):
        self.x_cord = coords[0]
        self.y_cord = coords[1]
        self.movespeed = movespeed
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.cd = cd

        self.mRight = False
        self.mLeft = False

        self.pl_move_sprites = AnimatedWalkingSprite()
        self.pl_sprite_list =arcade.SpriteList()


    """
    Moving function
    """
    def set_x_move(self):
        if not self.mLeft and self.mRight:
            self.pl_move_sprites.change_x = self.movespeed

        elif self.mLeft and not self.mRight:
            self.pl_move_sprites.change_x = -self.movespeed

        else:
            self.pl_move_sprites.change_x = 0


    """
    Check for out-of-bounds
    """
    def out_of_bounds(self):

        if self.pl_move_sprites.center_x <= 0:
            self.pl_move_sprites.center_x = 0
            self.pl_move_sprites.change_x = 0
            
        elif self.pl_move_sprites.center_x >= 1024:
            self.pl_move_sprites.center_x = 1024
            self.pl_move_sprites.change_x = 0


    """
    Key press and key release functions
    """
    def move_key_press(self, symbol: int):
        if symbol == arcade.key.RIGHT:
            self.mRight = True
            self.set_x_move()

        elif symbol == arcade.key.LEFT:
            self.mLeft = True
            self.set_x_move()


    def move_key_release(self, symbol: int):
        if symbol == arcade.key.RIGHT:
            self.mRight = False
            self.set_x_move()

        elif symbol == arcade.key.LEFT:
            self.mLeft = False
            self.set_x_move()


    """
    Animation functions
    """
    def update_animation(self, delta_time: float):
        self.pl_sprite_list.update_animation(delta_time=delta_time)
        self.pl_sprite_list.update()

        self.out_of_bounds()


            
    def draw(self):
        self.pl_sprite_list.draw()