from arcade import AnimatedWalkingSprite

from math import sqrt
from arcade import Texture
from typing import (
    Any,
    cast,
    Dict,
    List,
    Optional,
    TYPE_CHECKING,
)

FACE_RIGHT = 1
FACE_LEFT = 2
FACE_UP = 3
FACE_DOWN = 4

class OverrideAnimatedWalkingSprite(AnimatedWalkingSprite):
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

        self.count_time = 0


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
        if (
            self.change_x > 0
            and self.change_y == 0
            and self.state != FACE_RIGHT
            and len(self.walk_right_textures) > 0
        ):
            self.state = FACE_RIGHT
            change_direction = True
        elif (
            self.change_x < 0
            and self.change_y == 0
            and self.state != FACE_LEFT
            and len(self.walk_left_textures) > 0
        ):
            self.state = FACE_LEFT
            change_direction = True
        elif (
            self.change_y < 0
            and self.change_x == 0
            and self.state != FACE_DOWN
            and len(self.walk_down_textures) > 0
        ):
            self.state = FACE_DOWN
            change_direction = True
        elif (
            self.change_y > 0
            and self.change_x == 0
            and self.state != FACE_UP
            and len(self.walk_up_textures) > 0
        ):
            self.state = FACE_UP
            change_direction = True
        elif (
            self.change_y == 0
            and self.change_x == 0
            and self.state != FACE_LEFT
            and len(self.walk_right_textures) > 0
        ):
            self.state = FACE_RIGHT
            change_direction = True


        if self.change_x == 0 and self.change_y == 0:
            if self.state == FACE_LEFT:
                texture_list = self.stand_left_textures
            elif self.state == FACE_RIGHT:
                texture_list = self.stand_right_textures


            if self.count_time < delta_time:
                self.count_time += delta_time / 7

            else:
                self.count_time = 0
                self.cur_texture_index += 1
                if self.cur_texture_index >= len(texture_list):
                    self.cur_texture_index = 0

                self.texture = texture_list[self.cur_texture_index]


        elif change_direction or distance >= self.texture_change_distance:
            self.last_texture_change_center_x = self.center_x
            self.last_texture_change_center_y = self.center_y

            if self.state == FACE_LEFT:
                texture_list = self.walk_left_textures
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError(
                        "update_animation was called on a sprite that doesn't have a "
                        "list of walk left textures."
                    )
            elif self.state == FACE_RIGHT:
                texture_list = self.walk_right_textures
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError(
                        "update_animation was called on a sprite that doesn't have a list of "
                        "walk right textures."
                    )
            elif self.state == FACE_UP:
                texture_list = self.walk_up_textures
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError(
                        "update_animation was called on a sprite that doesn't have a list of "
                        "walk up textures."
                    )
            elif self.state == FACE_DOWN:
                texture_list = self.walk_down_textures
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError(
                        "update_animation was called on a sprite that doesn't have a list of walk down textures."
                    )

            #TODO: каждую вторую воспроизвоить и менять true и false

            self.cur_texture_index += 1
            if self.cur_texture_index >= len(texture_list):
                self.cur_texture_index = 0

            self.texture = texture_list[self.cur_texture_index]

        if self._texture is None:
            print("Error, no texture set")
        else:
            self.width = self._texture.width * self.scale
            self.height = self._texture.height * self.scale
