import arcade
import arcade.gui as gui

from objects.player import Player
from objects.enemy import Enemy

import random


class GameView(arcade.View):
    def __init__(self, 
                width: int = 800, 
                height: int = 600):

        super().__init__()
        self.width = width
        self.height = height

        self.background = arcade.load_texture("sprites/background/Forest/Image without mist.png")
        self.game_time = 0
        self.player_death = False

        self.setup()


    def setup(self):
        self.player = Player("adventurer")

        self.enemies = [Enemy((random.choice([*list(range(-150, 0, 50)), *list(range(self.width, self.width+150, 50))]), 190)) 
                        for i in range(1)]
        
        """
        Init UI
        """
        """
        Activate UI manager
        """
        self.manager = gui.UIManager()
        self.manager.enable()
        
        """
        Create group of buttons (vertical grid)
        """
        self.v_box = gui.UIBoxLayout()

        """
        Create lables
        """
        self.points_label = gui.UILabel(text=f"Points: {self.player.points}", 
                                        text_color=(255, 0, 0, 255), 
                                        font_size=20)
        self.hp_label = gui.UILabel(text=f"HP: {self.player.hp}", 
                                    text_color=(255, 0, 0, 255), 
                                    font_size=20)

        """
        Add lables in the group
        """
        self.v_box.add(self.points_label.with_space_around(bottom=20))
        self.v_box.add(self.hp_label.with_space_around(bottom=20))

        """
        Create vidget
        """
        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                align_x=20,
                align_y=-20,
                child=self.v_box
                )
        )

    """
    Updating the keys (for player)
    """
    def on_key_press(self, symbol: int, modifiers: int):
        self.player.move_key_press(symbol=symbol)


    def on_key_release(self, symbol: int, modifiers: int):
        self.player.move_key_release(symbol=symbol)


    """
    Fight
    """
    #Delete enemy and added new
    def del_enemy(self, enemy: Enemy):
        if enemy.en_sprites.cur_texture_index == len(enemy.en_sprites.death_left_textures)-1:
            self.enemies.remove(enemy)
            for i in range(2+int(self.game_time/50)):
                self.enemies.append(Enemy((random.choice([*list(range(-150, 0, 50)), *list(range(self.width, self.width+150, 50))]), 190)))


    def death(self, enemy: Enemy):
        if self.player.hp <=0:
            #for ending cycle
            self.player_death = True

            from views.death_view import DeathView

            score = self.player.points
            #clear memory
            del self.player
            del self.enemies

            death_view = DeathView(width=self.width,
                                   height=self.height,
                                   score=score)
            self.window.show_view(death_view)

        if enemy.hp <=0:
            enemy.en_sprites.state_death = True

            #Update points label
            self.player.points += 1+int(self.game_time/50) #int faster than round
            self.points_label.text = f"Points: {self.player.points}"
            self.points_label.fit_content()


    def update_damage_resistance(self, enemy: Enemy):
        if (self.player.damage_resistance and 
            enemy.en_sprites.cur_texture_index == 0):
            self.player.damage_resistance = False

        if (enemy.damage_resistance and 
            self.player.pl_sprites.cur_texture_index == 0):
            enemy.damage_resistance = False
                

    def fight(self, enemy: Enemy):
        if abs(self.player.pl_sprites.center_x - enemy.en_sprites.center_x) <= 100:
            #enemy hurt 
            if self.player.state_attack and not enemy.damage_resistance:
                enemy.hurt(self.player.damage)
            #player hurt
            if enemy.state_attack and not self.player.damage_resistance and not self.player.jump_damage_resistance:
                self.player.hurt(enemy.damage)
                #update hp label
                self.hp_label.text = f"HP: {self.player.hp}"
                self.hp_label.fit_content()

            """
            Update damage resistance and check death
            """
            self.update_damage_resistance(enemy)
            self.death(enemy)


    """
    Updating
    """
    def on_update(self, delta_time: float):
        self.player.update(delta_time=delta_time)

        for enemy in self.enemies:
            if not self.player_death:
                enemy.update(delta_time=delta_time, player_x_cord=self.player.pl_sprites.center_x)
                self.del_enemy(enemy) if enemy.en_sprites.state_death == True else self.fight(enemy)

        self.game_time += delta_time

    """
    Draw objects
    """
    def on_draw(self):
        arcade.start_render()
        #background
        arcade.draw_texture_rectangle(self.width/2, self.height/2, width=self.width, height=self.height, texture=self.background)

        #enemy and player
        for enemy in self.enemies:
            enemy.draw()

        self.player.draw()

        #lables
        self.manager.draw()