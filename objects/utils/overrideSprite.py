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
        #States
        self.__state_x = RIGHT
        self.__state_y = STAND
        self.state_attack: bool = False
        self.state_hurt: bool = False
        self.state_death:bool = False

        #Sprites
        self.stand_right_textures: List[Texture] = []
        self.stand_left_textures: List[Texture] = []
        self.walk_right_textures: List[Texture] = []
        self.walk_left_textures: List[Texture] = []
        self.jump_right_textures: List[Texture] = []
        self.jump_left_textures: List[Texture] = []
        self.fall_right_textures: List[Texture] = []
        self.fall_left_textures: List[Texture] = []
        self.attack_right_textures: List[Texture] = []
        self.attack_left_textures: List[Texture] = []
        self.hurt_right_textures: List[Texture] = []
        self.hurt_left_textures: List[Texture] = []
        self.death_right_textures: List[Texture] = []
        self.death_left_textures: List[Texture] = []

        #Oher
        self.cur_texture_index = 0

        self.texture_change_distance = 20
        self.last_texture_change_center_x: float = 0
        self.last_texture_change_center_y: float = 0

        self.__idle_sprite_show_counter = 0

        #Debug
        self.debug = False


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
            and self.__state_x != RIGHT
        ):
            self.__state_x = RIGHT
            change_direction = True
        elif (
            self.change_x < 0
            and self.__state_x != LEFT
        ):
            self.__state_x = LEFT
            change_direction = True
        """
        Direction y
        """
        if (
            self.change_y < 0
            and self.__state_y != FALL
        ):
            self.__state_y = FALL
            change_direction = True
        elif (
            self.change_y > 0
            and self.__state_y != JUMP
        ):
            self.__state_y = JUMP
            change_direction = True
        elif (
            self.change_y == 0
            and self.change_x == 0
            and self.__state_y != STAND
        ):
            self.__state_y = STAND
            change_direction = True
        elif (
            self.change_y == 0 
            and self.change_x != 0
            and self.__state_y != WALK
        ):
            self.__state_y = WALK
            change_direction = True

            
        """
        Load sprites
        """
        #Death
        if self.state_death:
            if self.__state_x == LEFT:
                texture_list = self.death_left_textures

            elif self.__state_x == RIGHT:
                texture_list = self.death_right_textures

            self.texture_change_distance = 20
            self.slowed_change_sprite(texture_list, 8)   
        #Hurt
        elif self.state_hurt:
            if self.__state_x == LEFT:
                texture_list = self.hurt_left_textures

            elif self.__state_x == RIGHT:
                texture_list = self.hurt_right_textures

            self.texture_change_distance = 20
            self.slowed_change_sprite(texture_list, 8)

        #Attack
        elif self.state_attack:
            if self.__state_x == LEFT:
                texture_list = self.attack_left_textures

            elif self.__state_x == RIGHT:
                texture_list = self.attack_right_textures

            self.texture_change_distance = 20
            self.slowed_change_sprite(texture_list, 4)

        #IDLE
        elif self.__state_y == STAND:
            if self.__state_x == LEFT:
                texture_list = self.stand_left_textures

            elif self.__state_x == RIGHT:
                texture_list = self.stand_right_textures

            self.texture_change_distance = 20
            self.slowed_change_sprite(texture_list, 6)    

        #Move         
        elif change_direction or distance >= self.texture_change_distance:
            self.last_texture_change_center_x = self.center_x
            self.last_texture_change_center_y = self.center_y

            if self.__state_y == WALK:  
                if self.__state_x == RIGHT:
                    texture_list = self.walk_right_textures

                elif self.__state_x == LEFT:
                    texture_list = self.walk_left_textures

                self.texture_change_distance = 20
                self.change_sprite(texture_list)
 

            elif self.__state_y == FALL:
                if self.__state_x == RIGHT:
                    texture_list = self.fall_right_textures

                elif self.__state_x == LEFT:
                    texture_list = self.fall_left_textures

                self.texture_change_distance = 20
                self.change_sprite(texture_list)
 
                
            elif self.__state_y == JUMP:
                if self.__state_x == RIGHT:
                    texture_list = self.jump_right_textures

                elif self.__state_x == LEFT:
                    texture_list = self.jump_left_textures

                self.texture_change_distance = 60
                self.slowed_change_sprite(texture_list, 4)

            """
            Reset cursor and counter
            """
            if change_direction:
                self.cur_texture_index = 0
                self.__idle_sprite_show_counter = 0

        
        if self._texture:
            self.width = self._texture.width * self.scale
            self.height = self._texture.height * self.scale

        self.update()

        """
        Debug
        """
        if self.debug:
            print(change_direction,
                len(texture_list),
                self.__state_y,
                self.__state_x, 
                distance,
                self.state_attack,
                self.cur_texture_index,
                self.change_x,
                self.change_y
            )


    """
    For slowing animation
    """
    def slowed_change_sprite(self, texture_list, slow):
            if self.__idle_sprite_show_counter == slow:
                self.change_sprite(texture_list)
                self.__idle_sprite_show_counter=0

            self.__idle_sprite_show_counter+=1


    def change_sprite(self, texture_list):
        if texture_list is None or len(texture_list) == 0:
            raise RuntimeError(
                "update_animation was called on a sprite that doesn't have a list of textures."
            )

        self.cur_texture_index += 1
        if self.cur_texture_index >= len(texture_list):
            self.cur_texture_index = 0

        self.texture = texture_list[self.cur_texture_index]       