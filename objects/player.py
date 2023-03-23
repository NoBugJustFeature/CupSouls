import arcade

from objects.game_object import Game_object
from objects.player_variable import adventurer as adv


class Player(Game_object):
    def __init__(self, hero: str = "adventurer"):
        """
        Load
        """
        if hero == "adventurer":
            super().__init__(coords=adv.get("coords"),
                            movespeed=adv.get("movespeed"), 
                            jump_height=adv.get("jump_height"),
                            jump_speed=adv.get( "jump_speed"),
                            hp=adv.get("hp"), 
                            damage=adv.get("da"),
                            armor=adv.get("armor"), 
                            cd=adv.get("cd"))

            self.adventurer_load_animation()


    """
    Load sprites
    """
    def adventurer_load_animation(self):

        """
        IDLE animation
        """
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
        self.pl_sprites.jump_right_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-jump-0{num}.png") for num in range(4)]

        self.pl_sprites.jump_left_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-jump-0{num}.png", mirrored=True)
                for num in range(4)]

        """
        Fall animation
        """
        self.pl_sprites.fall_right_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-jump-00.png")]

        self.pl_sprites.fall_left_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-jump-00.png", mirrored=True)]

        """
        Set variables
        """
        self.pl_sprites.scale = adv.get("scale")
        self.pl_sprites.center_x = self.x_cord
        self.pl_sprites.center_y = self.y_cord

        self.pl_sprite_list.append(self.pl_sprites)