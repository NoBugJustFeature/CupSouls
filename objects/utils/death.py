from objects.player import Player
from objects.enemy import Enemy


def death(player: Player, enemies: list[Enemy]):
    if player.hp <=0:
        print("pl death")
    for enemy in enemies:
        if enemy.hp <=0:
            print("en death")