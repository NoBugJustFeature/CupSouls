from typing import Tuple
import arcade

from objects.utils.overrideSprite \
    import OverrideSprite as Sprite

from variables import WIDTH, HEIGHT


"""
Directions
"""
RIGHT = 0
LEFT = 1


class Player_object():
    def __init__(self, 
                coords: Tuple[float, float],
                movespeed: float,
                dash_distance_mult: float,
                jump_height: float,
                jump_speed: float,
                hp: int, 
                damage: float, 
                armor: int, #similar hp, but can recovery
                armor_cd: float #armor recovery time (in seconds)
                ):
        self.x_cord = coords[0]
        self.y_cord = coords[1]
        self.movespeed = movespeed
        self.dash_distance = self.movespeed * dash_distance_mult
        self.jump_height = jump_height
        self.jump_speed = jump_speed
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.armor_cd = armor_cd

        self.state_right = False
        self.state_left = False
        self.state_jump = False
        self.state_attack = False
        self.damage_resistance = False
        self.state_dash = False

        self.jump_max_height=0

        self.gravity_constant: float = 5
        self.floor_constant: int = 175 # = self.y_cord

        self.pl_sprites = Sprite()
        self.pl_sprite_list = arcade.SpriteList()


    """
    Moving function
    """
    def set_x_move(self):
        if not self.state_left and self.state_right:
            self.pl_sprites.change_x = self.movespeed

        elif self.state_left and not self.state_right:
            self.pl_sprites.change_x = -self.movespeed

        else:
            self.pl_sprites.change_x = 0


    def set_y_move(self):
        if self.state_jump and self.pl_sprites.center_y == self.floor_constant:
            self.pl_sprites.change_y = self.jump_speed

        elif not self.state_jump and self.pl_sprites.center_y != self.floor_constant:
            self.pl_sprites.change_y = 0

    
    def gravity(self):
        if self.pl_sprites.center_y > self.floor_constant and not self.state_jump:
            self.pl_sprites.change_y = -self.gravity_constant

        elif self.pl_sprites.center_y <= self.floor_constant and not self.state_jump:
            self.pl_sprites.change_y = 0


    #use it func in on_update
    def update_jump(self):
        if self.pl_sprites.center_y >= self.jump_max_height:
            self.state_jump = False
            self.jump_max_height = 0
            self.set_y_move()
        

    """
    Check for out-of-bounds
    """
    def out_of_bounds(self):

        if self.pl_sprites.center_x <= 0:
            self.pl_sprites.center_x = 0
            self.pl_sprites.change_x = 0
            
        elif self.pl_sprites.center_x >= WIDTH:
            self.pl_sprites.center_x = WIDTH
            self.pl_sprites.change_x = 0

        if self.pl_sprites.center_y <= self.floor_constant:
            self.pl_sprites.center_y = self.floor_constant
            self.pl_sprites.change_y = 0
            
        elif self.pl_sprites.center_y >= HEIGHT:
            self.pl_sprites.center_y = HEIGHT
            self.pl_sprites.change_y = 0


    """
    Attack function
    """
    def attack(self):
        self.pl_sprites.state_attack = self.state_attack


    """
    Dash finction
    """
    def dash(self, direction):
        if not self.state_dash:
            self.state_dash = True
            self.damage_resistance = True
            if direction == RIGHT:
                self.pl_sprites.center_x += self.movespeed*25
            elif direction == LEFT:
                self.pl_sprites.center_x -= self.movespeed*25
            

    """
    Key press and key release functions
    """
    def move_key_press(self, symbol: int):
        if symbol == arcade.key.Z:
            self.dash(LEFT)
        elif symbol == arcade.key.C:
            self.dash(RIGHT)

        if symbol == arcade.key.RIGHT:
            self.state_right = True
            self.set_x_move()

        elif symbol == arcade.key.LEFT:
            self.state_left = True
            self.set_x_move()

        if symbol == arcade.key.UP or symbol == arcade.key.SPACE:
            self.state_jump = True
            self.jump_max_height = self.pl_sprites.center_y + self.jump_height

            self.set_y_move()

        if symbol == arcade.key.X:
            self.state_attack = True
            self.attack()

        """
        Debug key
        """
        if symbol == arcade.key.TAB:
            self.pl_sprites.debug = True
    

    def move_key_release(self, symbol: int):
        if symbol == arcade.key.RIGHT:
            self.state_right = False
            self.set_x_move()

        elif symbol == arcade.key.LEFT:
            self.state_left = False
            self.set_x_move()

        if symbol == arcade.key.UP or symbol == arcade.key.SPACE:
            self.state_jump = False
            self.jump_max_height = 0
            self.set_y_move()

        if symbol == arcade.key.X:
            self.state_attack = False
            self.attack()

        if symbol == arcade.key.Z or symbol == arcade.key.C:
            self.state_dash = False
            self.damage_resistance = False

        """
        Debug key
        """
        if symbol == arcade.key.TAB:
            self.pl_sprites.debug = False
    



    """
    Update functions
    """
    def update(self, delta_time: float):
        self.pl_sprite_list.update_animation(delta_time=delta_time)

        self.out_of_bounds()

        self.update_jump()
        self.gravity()


    def draw(self):
        self.pl_sprite_list.draw()