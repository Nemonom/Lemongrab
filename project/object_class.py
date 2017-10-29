import  global_parameters
import random
from pico2d import *


class player:
    def __init__(self):
        self.img = load_image('player.png')
        self.hp = global_parameters.player_hp
        self.mp = global_parameters.player_mp
        self.spd = global_parameters.player_spd
        self.att = global_parameters.player_att
        self.size_x = global_parameters.player_size_x
        self.size_y = global_parameters.player_size_y
        self.frame = 0

    def draw(self, angle):
        self.img.rotate_draw(angle, 500, 350, self.size_x, self.size_y)


class enemy:
    size_x, size_y = None, None

    def __init__(self):
        if enemy.img == None:
            img = load_image('enemy.png')
        size_x, size_y = global_parameters.mon_size_x, global_parameters.mon_size_y


