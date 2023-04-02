from typing import Tuple
import arcade

from objects.enemy_object import Enemy_object
from objects.enemy_variable import DarkKnight as DK

class Enemy (Enemy_object):
    """
    Load
    """
    def __init__(self, coords: Tuple[float, float]):
        super().__init__(coords=coords,
                        movespeed=DK.get("movespeed"), 
                        hp=DK.get("hp"), 
                        damage=DK.get("damage"),
                        frames_befor_attack=DK.get("frames_befor_attack"),
                        frames_hurt=DK.get("frames_hurt"))

        self.DK_load_animation()


    """
    Load sprites
    """
    def DK_load_animation(self):
        """
        IDLE animation
        """
        self.en_sprites.stand_right_textures = [
            arcade.load_texture(f"sprites/enemies/DarkKnight/NightBorne.png",
            x=80*i,
            y=0,
            width=80,
            height=80) 
            for i in range(9)]

        self.en_sprites.stand_left_textures = [
            arcade.load_texture(f"sprites/enemies/DarkKnight/NightBorne.png",
            x=80*i,
            y=0,
            width=80,
            height=80,
            mirrored=True) 
            for i in range(9)]

        """
        Walk animation
        """
        self.en_sprites.walk_right_textures = [
            arcade.load_texture(f"sprites/enemies/DarkKnight/NightBorne.png",
            x=80*i,
            y=80,
            width=80,
            height=80) 
            for i in range(6)]

        self.en_sprites.walk_left_textures = [
            arcade.load_texture(f"sprites/enemies/DarkKnight/NightBorne.png",
            x=80*i,
            y=80,
            width=80,
            height=80,
            mirrored=True) 
            for i in range(6)]

        """
        Attack animation
        """
        self.en_sprites.attack_right_textures = [
            arcade.load_texture(f"sprites/enemies/DarkKnight/NightBorne.png",
            x=80*i,
            y=160,
            width=80,
            height=80) 
            for i in range(12)]

        self.en_sprites.attack_left_textures = [
            arcade.load_texture(f"sprites/enemies/DarkKnight/NightBorne.png",
            x=80*i,
            y=160,
            width=80,
            height=80,
            mirrored=True) 
            for i in range(12)]

        """
        Hurt animation
        """
        self.en_sprites.hurt_right_textures = [
            arcade.load_texture(f"sprites/enemies/DarkKnight/NightBorne.png",
            x=80*i,
            y=240,
            width=80,
            height=80) 
            for i in range(5)]

        self.en_sprites.hurt_left_textures = [
            arcade.load_texture(f"sprites/enemies/DarkKnight/NightBorne.png",
            x=80*i,
            y=240,
            width=80,
            height=80,
            mirrored=True) 
            for i in range(5)]
        
        """
        Hurt animation
        """
        self.en_sprites.death_right_textures = [
            arcade.load_texture(f"sprites/enemies/DarkKnight/NightBorne.png",
            x=80*i,
            y=320,
            width=80,
            height=80) 
            for i in range(23)]

        self.en_sprites.death_left_textures = [
            arcade.load_texture(f"sprites/enemies/DarkKnight/NightBorne.png",
            x=80*i,
            y=320,
            width=80,
            height=80,
            mirrored=True) 
            for i in range(23)]

        """
        Set variables
        """
        self.en_sprites.scale = DK.get("scale")
        self.en_sprites.center_x = self.x_cord
        self.en_sprites.center_y = self.y_cord

        self.en_sprite_list.append(self.en_sprites)


