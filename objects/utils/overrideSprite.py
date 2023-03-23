from arcade import Sprite

from math import sqrt
from arcade import Texture
from typing import List


"""
Direction variables
"""
#Direction x
RIGHT = 0
LEFT = 1

#Direction y
STAND = 0
WALK = 1
JUMP = 2
FALL = 3



class OverrideSprite(Sprite):
    def __init__(
        self,
        scale: float = 1,
        image_x: float = 0,
        image_y: float = 0,
        center_x: float = 0,
        center_y: float = 0,
    ):
        super().__init__(
            scale=scale,
            image_x=image_x,
            image_y=image_y,
            center_x=center_x,
            center_y=center_y,
        )

        """
        Variables
        """
        #Direction
        self.state_x = RIGHT
        self.state_y = STAND

        #Sprites
        self.stand_right_textures: List[Texture] = []
        self.stand_left_textures: List[Texture] = []
        self.walk_right_textures: List[Texture] = []
        self.walk_left_textures: List[Texture] = []
        self.jump_right_textures: List[Texture] = []
        self.jump_left_textures: List[Texture] = []
        self.fall_right_textures: List[Texture] = []
        self.fall_left_textures: List[Texture] = []

        #Oher
        self.cur_texture_index = 0

        self.texture_change_distance = 20
        self.last_texture_change_center_x: float = 0
        self.last_texture_change_center_y: float = 0

        self.idle_sprite_show_counter = 0


    def update_animation(self, delta_time: float = 1 / 60, duration: float = 1/60):
        """
        Logic for selecting the proper texture to use.
        """
        x1 = self.center_x
        x2 = self.last_texture_change_center_x
        y1 = self.center_y
        y2 = self.last_texture_change_center_y
        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        texture_list: List[Texture] = []

        change_direction = False
        """
        Direction x
        """
        if (
            self.change_x > 0
            and self.state_x != RIGHT
        ):
            self.state_x = RIGHT
            change_direction = True
        elif (
            self.change_x < 0
            and self.state_x != LEFT
        ):
            self.state_x = LEFT
            change_direction = True
        """
        Direction y
        """
        if (
            self.change_y < 0
            and self.state_y != FALL
        ):
            self.state_y = FALL
            change_direction = True
        elif (
            self.change_y > 0
            and self.change_x == 0
            and self.state_y != JUMP
        ):
            self.state_y = JUMP
            change_direction = True
        elif (
            self.change_y == 0
            and self.change_x == 0
            and self.state_y != STAND
        ):
            self.state_y = STAND
            change_direction = True
        elif (
            self.change_y == 0 
            and self.change_x != 0
            and self.state_y != WALK
        ):
            self.state_y = WALK
            change_direction = True


        """
        IDLE
        """
        if self.state_y == STAND:
            if self.state_x == LEFT:
                texture_list = self.stand_left_textures
                print("stand left")
            elif self.state_x == RIGHT:
                print("stand right")
                texture_list = self.stand_right_textures

            """
            For slowing animation
            """
            if self.idle_sprite_show_counter == 7:
                self.change_sprite(texture_list)
                self.idle_sprite_show_counter=0

            self.idle_sprite_show_counter+=1      

            """
            Move
            """
        elif change_direction or distance >= self.texture_change_distance:
            self.last_texture_change_center_x = self.center_x
            self.last_texture_change_center_y = self.center_y

            if self.state_y == FALL:
                if self.state_x == RIGHT:
                    texture_list = self.fall_right_textures
                    print("fall right")
                elif self.state_x == LEFT:
                    texture_list = self.fall_left_textures
                    print("fall left")
                self.texture_change_distance = 20
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError(
                        "update_animation was called on a sprite that doesn't have a list of textures."
                    )

            elif self.state_y == JUMP:
                if self.state_x == RIGHT:
                    texture_list = self.jump_right_textures
                    print("jump right")
                elif self.state_x == LEFT:
                    texture_list = self.jump_left_textures
                    print("jump left")
                self.texture_change_distance = 60
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError(
                        "update_animation was called on a sprite that doesn't have a list of textures."
                    )

            elif self.state_y == WALK:
                if self.state_x == RIGHT:
                    print("walk right")
                    texture_list = self.walk_right_textures
                elif self.state_x == LEFT:
                    print("walk left")
                    texture_list = self.walk_left_textures
                self.texture_change_distance = 20
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError(
                        "update_animation was called on a sprite that doesn't have a list of textures."
                    )
              

            self.change_sprite(texture_list)

        if self._texture is None:
            print("Error, no texture set")
        else:
            self.width = self._texture.width * self.scale
            self.height = self._texture.height * self.scale


    def change_sprite(self, texture_list):
            self.cur_texture_index += 1
            if self.cur_texture_index >= len(texture_list):
                self.cur_texture_index = 0

            self.texture = texture_list[self.cur_texture_index]


            
