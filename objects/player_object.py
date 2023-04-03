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
                frames_hurt: int
                ):
        self.x_cord = coords[0]
        self.y_cord = coords[1]
        self.movespeed = movespeed
        self.dash_distance = self.movespeed * dash_distance_mult
        self.jump_height = jump_height
        self.jump_speed = jump_speed
        self.hp = hp
        self.damage = damage

        """
        Other
        """
        self.points = 0
        self.press_attack = True

        """
        States
        """
        self.state_right = False
        self.state_left = False
        self.state_jump = False
        self.state_attack = False
        self.damage_resistance = False
        self.jump_damage_resistance = False #костыль
        self.state_dash = False

        """
        Jump
        """
        self.gravity_constant: float = 5
        self.floor_constant: int = 175 # = self.y_cord
        self.jump_max_height=0

        """
        Sprites
        """
        self.frames_hurt = frames_hurt
        self.pl_sprites = Sprite()
        self.pl_sprite_list = arcade.SpriteList()

        self.c = 0


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
            self.jump_damage_resistance = True

    
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

        self.jump_damage_resistance = True if self.pl_sprites.center_y != self.floor_constant else False
        

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
        self.pl_sprites.state_attack = self.state_attack = True

    def update_frame_attack(self):
        if self.pl_sprites.state_attack and self.pl_sprites.cur_texture_index == len(self.pl_sprites.attack_right_textures)-1:
            self.pl_sprites.state_attack = self.state_attack = False
    """
    Dash finction
    """
    def dash(self, direction: str = ""):
        if self.state_dash:
            self.state_dash = False
            self.damage_resistance = True
            if direction == RIGHT:
                self.pl_sprites.center_x += self.movespeed*25
            elif direction == LEFT:
                self.pl_sprites.center_x -= self.movespeed*25
        else:
            self.damage_resistance = False


    """
    Hurt
    """
    def hurt(self, damage: float):
        self.hp -= damage
        self.pl_sprites.state_hurt = True
        self.damage_resistance = True

    def update_frame_hitted(self):
        if self.pl_sprites.state_hurt == True and self.pl_sprites.cur_texture_index == len(self.pl_sprites.hurt_right_textures)-1:
            self.pl_sprites.state_hurt = False

            

    """
    Key press and key release functions
    """
    def move_key_press(self, symbol: int):
        if not self.pl_sprites.state_hurt:
            if symbol == arcade.key.Z:
                self.state_dash = True
                self.dash(LEFT)
            elif symbol == arcade.key.C:
                self.state_dash = True
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
            self.press_attack = False

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

        self.update_frame_hitted()
        self.update_frame_attack()


    def draw(self):
        self.pl_sprite_list.draw()