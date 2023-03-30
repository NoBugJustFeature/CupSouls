from objects.player import Player
from objects.enemy import Enemy

from objects.utils.death import death

def fight(player: Player, enemies: list[Enemy]):
    for enemy in enemies:
        if abs(player.pl_sprites.center_x - enemy.en_sprites.center_x) <= 100:
            if player.state_attack and not enemy.en_sprites.state_hurt:
                enemy.hurt(player.damage)
            if enemy.state_attack and not player.pl_sprites.state_hurt:
                player.hurt(enemy.damage)

            death(player, enemies)