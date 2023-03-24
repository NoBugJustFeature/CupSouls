from typing import Tuple
import arcade

from objects.utils.overrideSprite \
    import OverrideSprite as Sprite

from variables import WIDTH, HEIGHT


class Game_object():
    def __init__(self, 
                coords: Tuple[float, float],
                movespeed: float,
                jump_height: float,
                jump_speed: float,
                hp: int, 
                damage: float, 
                armor: int, #similar hp, but can recovery
                cd: float #armor recovery time (in seconds)
                ):
        self.x_cord = coords[0]
        self.y_cord = coords[1]
        self.movespeed = movespeed
        self.jump_height = jump_height
        self.jump_speed = jump_speed
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.cd = cd

        self.mRight = False
        self.mLeft = False
        self.mJump = False
        self.sAttack = False

        self.jump_time = 0
        self.jump_time_max = 2
        self.jump_max_height=0

        self.c = 0

        self.gravity_constant: float = 5
        self.floor_constant: int = 175 # = self.y_cord

        self.pl_sprites = Sprite()
        self.pl_sprite_list = arcade.SpriteList()


    """
    Moving function
    """
    def set_x_move(self):
        if not self.mLeft and self.mRight:
            self.pl_sprites.change_x = self.movespeed

        elif self.mLeft and not self.mRight:
            self.pl_sprites.change_x = -self.movespeed

        else:
            self.pl_sprites.change_x = 0


    def set_y_move(self):
        if self.mJump and self.pl_sprites.center_y == self.floor_constant:
            self.pl_sprites.change_y = self.jump_speed

        elif not self.mJump and self.pl_sprites.center_y != self.floor_constant:
            self.pl_sprites.change_y = 0

    
    def gravity(self):
        if self.pl_sprites.center_y > self.floor_constant and not self.mJump:
            self.pl_sprites.change_y = -self.gravity_constant

        elif self.pl_sprites.center_y <= self.floor_constant and not self.mJump:
            self.pl_sprites.change_y = 0


    #use it func in on_update
    def update_jump(self):
        if self.pl_sprites.center_y >= self.jump_max_height:
            self.mJump = False
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
        
        self.pl_sprites.state_attack = self.sAttack
        


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

        if symbol == arcade.key.UP or symbol == arcade.key.SPACE:
            self.mJump = True
            self.jump_max_height = self.pl_sprites.center_y + self.jump_height
            self.set_y_move()

        if symbol == arcade.key.Z:
            self.sAttack = True
            self.attack()

        """
        Debug key
        """
        if symbol == arcade.key.TAB:
            self.pl_sprites.debug = True
    

    def move_key_release(self, symbol: int):
        if symbol == arcade.key.RIGHT:
            self.mRight = False
            self.set_x_move()

        elif symbol == arcade.key.LEFT:
            self.mLeft = False
            self.set_x_move()

        if symbol == arcade.key.UP or symbol == arcade.key.SPACE:
            self.mJump = False
            self.jump_max_height = 0
            self.set_y_move()

        if symbol == arcade.key.Z:
            self.sAttack = False
            self.attack()

        """
        Debug key
        """
        if symbol == arcade.key.TAB:
            self.pl_sprites.debug = False
    



    """
    Animation functions
    """
    def update_animation(self, delta_time: float):
        self.pl_sprite_list.update_animation(delta_time=delta_time)

        self.out_of_bounds()
        self.gravity()


    def draw(self):
        self.pl_sprite_list.draw()