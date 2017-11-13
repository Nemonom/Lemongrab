import math
import global_parameters
import game_state
import random
from pico2d import *

class player:

    def __init__(self):
        self.img = load_image('normal_state.png')
        self.hp = global_parameters.player_hp
        self.mp = global_parameters.player_mp
        self.spd = global_parameters.player_spd
        self.att = global_parameters.player_att
        self.size_x = global_parameters.player_size_x
        self.size_y = global_parameters.player_size_y
        self.angle = 0
        self.frame = 0
        self.attack_ing = False

    def draw(self):
        self.img.rotate_draw(self.angle, 500, 350, self.size_x, self.size_y)

    def get_angle(self, event_x, event_y):
        self.angle = math.atan2((global_parameters.height/2 - event_y) , (global_parameters.width/2 - event_x))

        pass

    def return_hp(self):
        return self.hp

    def return_mp(self):
        return self.mp

    def return_attack(self):
        return self.attack_ing

    def get_bb(self):
        return self.x - self.size_x / 2, self.y - self.size_y / 2\
            , self.x + self.size_x / 2, self.y + self.size_y / 2



class enemy:
    size_x, size_y = None, None
    img = None
    RELAX, CHASE, ATTACK = 0, 1, 2

    def __init__(self):
        if enemy.img == None:
            img = load_image('enemy.png')
        enemy.size_x, enemy.size_y = global_parameters.mon_size_x, global_parameters.mon_size_y



class item:
    size_x, size_y = None, None

    def __init__(self, what, x, y):
        self.type = what
        self.x, self.y = x, y
        if what == 0:
            self.img = load_image('lemon.png')
        elif what == 1:
            self.img = load_image('hp.png')
        elif what == 2:
            self.img = load_image('mp.png')


    def return_type(self):
        return self.type

    def draw(self):
        self.img.draw(self.x, self.y, item.size_x, item.size_y)

    def get_bb(self):
        return self.x - item.size_x/2, self.y - item.size_y/2, self.x + item.size_x/2, self.y + item.size_y/2

#game state에 있는 변수값 여기서 type 따져서 바로 바꿔줘



class bullet:
    size_x, size_y = None, None

    def __init__(self, x, y, event_x, event_y):
        self.x, self.y = global_parameters.width/2, global_parameters.height/2
        self.angle = math.atan2((global_parameters.height/2 - event_y) , (global_parameters.width/2 - event_x))
         self.img = load_image('lemon.png')

    def update(self):
        pass

    def draw(self):
        self.img.rotate_draw(self.angle, 500, 350, self.size_x, self.size_y)

    def get_bb(self):
        return self.x - item.size_x/2, self.y - item.size_y/2, self.x + item.size_x/2, self.y + item.size_y/2