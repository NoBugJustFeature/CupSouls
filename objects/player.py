import arcade

from objects.game_object import Game_object
from objects.player_variable import adventure


class Player(Game_object):
    def __init__(self):
        super().__init__(coords=(500, 175),
                        movespeed=adventure.get("movespeed"), 
                        hp=adventure.get("hp"), 
                        damage=adventure.get("da"),
                        armor=adventure.get("armor"), 
                        cd=adventure.get("cd"))


        self.pl_move_sprites = arcade.AnimatedWalkingSprite(scale=4)

        self.pl_move_sprites.stand_right_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-idle-0{num}.png") for num in range(4)]

        self.pl_move_sprites.stand_left_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-idle-0{num}.png", mirrored= True) 
            for num in range(4)]

        self.pl_move_sprites.walk_right_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-run-0{num}.png") for num in range(6)]

        self.pl_move_sprites.walk_left_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-run-0{num}.png", mirrored= True)
            for num in range(6)]

        self.pl_move_sprites.center_x = self.x_cord
        self.pl_move_sprites.center_y = self.y_cord

        self.pl_sprite_list = arcade.SpriteList()
        self.pl_sprite_list.append(self.pl_move_sprites)
                                    

        self.mRight = False
        self.mLeft = False



    def set_x_move(self):
        if not self.mLeft and self.mRight:
            self.pl_move_sprites.change_x = self.movespeed

        elif self.mLeft and not self.mRight:
            self.pl_move_sprites.change_x = -self.movespeed

        else:
            self.pl_move_sprites.change_x = 0


    def out_of_bounds(self):
        # Check for out-of-bounds
        if self.pl_move_sprites.center_x <= 0:
            self.pl_move_sprites.center_x = 0
            self.pl_move_sprites.change_x = 0
            
        elif self.pl_move_sprites.center_x >= 1024:
            self.pl_move_sprites.center_x = 1024
            self.pl_move_sprites.change_x = 0


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


    def update(self, delta_time: float):
        self.pl_sprite_list.update_animation(delta_time=delta_time)
        self.pl_sprite_list.update()

        self.out_of_bounds()


            
    def draw(self):
        self.pl_sprite_list.draw()


