import arcade

from objects.game_object import Game_object
from objects.player_variable import adventurer


class Player(Game_object):
    def __init__(self, hero: str = "adventurer"):
        """
        Load
        """
        if hero == "adventurer":
            super().__init__(coords=adventurer.get("coords"),
                            movespeed=adventurer.get("movespeed"), 
                            jump_height=adventurer.get("jump_height"),
                            jump_speed=adventurer.get( "jump_speed"),
                            hp=adventurer.get("hp"), 
                            damage=adventurer.get("da"),
                            armor=adventurer.get("armor"), 
                            cd=adventurer.get("cd"))

            self.adventurer_load_animation()


    """
    Load sprites
    """
    def adventurer_load_animation(self):
        """
        IDLE animation
        """
        self.pl_sprites.scale = adventurer.get("scale")

        self.pl_sprites.stand_right_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-idle-0{num}.png") for num in range(4)]

        self.pl_sprites.stand_left_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-idle-0{num}.png", mirrored=True) 
            for num in range(4)]

        """
        Walk animation
        """
        self.pl_sprites.walk_right_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-run-0{num}.png") for num in range(6)]

        self.pl_sprites.walk_left_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-run-0{num}.png", mirrored=True)
            for num in range(6)]


        """
        Jump animation
        """
        self.pl_sprites.walk_up_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-jump-0{num}.png") for num in range(4)]
        self.pl_sprites.walk_down_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-jump-00.png")]

        """
        Set variables
        """
        self.pl_sprites.center_x = self.x_cord
        self.pl_sprites.center_y = self.y_cord

        self.pl_sprite_list.append(self.pl_sprites)