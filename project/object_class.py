import  global_parameters
import random
import math
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
        self.angle = 0
        self.frame = 0

    def draw(self):
        self.img.rotate_draw(self.angle, 500, 350, self.size_x, self.size_y)

    def get_angle(self, event_x, event_y):
        self.angle = math.atan(event_x/event_y)
        pass



class enemy:
    size_x, size_y = None, None
    img = None
    RELAX, CHASE, ATTACK, GET_ATTACK = 0, 1, 2, 3

    def __init__(self):
        if enemy.img == None:
            img = load_image('enemy.png')
        enemy.size_x, enemy.size_y = global_parameters.mon_size_x, global_parameters.mon_size_y


