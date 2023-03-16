from typing import Tuple

class Game_object():
    def __init__(self, 
                coords: Tuple[float, float],
                movespeed: float,
                hp: int, 
                damage: float, 
                armor: int, 
                cd: float):
        self.x_cord = coords[0]
        self.y_cord = coords[1]
        self.movespeed = movespeed
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.cd = cd

