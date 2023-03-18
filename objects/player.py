import arcade

from objects.game_object import Game_object
from objects.player_variable import adventurer

from objects.utils.overrideAnimatedWalkingSprite \
    import OverrideAnimatedWalkingSprite as AnimatedWalkingSprite


class Player(Game_object):
    def __init__(self):
        """
        Load
        """
        super().__init__(coords=adventurer.get("coords"),
                        movespeed=adventurer.get("movespeed"), 
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
        self.pl_move_sprites.scale = adventurer.get("scale")

        self.pl_move_sprites.stand_right_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-idle-0{num}.png") for num in range(4)]

        self.pl_move_sprites.stand_left_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-idle-0{num}.png", mirrored=True) 
            for num in range(4)]

        """
        Walk animation
        """
        self.pl_move_sprites.walk_right_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-run-0{num}.png") for num in range(6)]

        self.pl_move_sprites.walk_left_textures = [
            arcade.load_texture(f"sprites/player/adventure/adventurer-run-0{num}.png", mirrored=True)
            for num in range(6)]

        """
        Set variables
        """
        self.pl_move_sprites.center_x = self.x_cord
        self.pl_move_sprites.center_y = self.y_cord

        self.pl_sprite_list.append(self.pl_move_sprites)