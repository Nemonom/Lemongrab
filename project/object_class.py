import math
import global_parameters
import game_state
import random
from pico2d import *

#player class
class player:

    def __init__(self):
        self.img = load_image('head.png')
        self.hp = global_parameters.player_hp
        self.mp = global_parameters.player_mp
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


#enemy class
class enemy:
    size_x, size_y = None, None
    img = None
    RELAX, CHASE, ATTACK = 0, 1, 2

    def __init__(self, m_x, m_y):
        if enemy.img == None:
            img = load_image('enemy.png')
        enemy.size_x, enemy.size_y = global_parameters.mon_size_x, global_parameters.mon_size_y
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = m_x, m_y
        self.hp = global_parameters.mon_hp
        self.att = global_parameters.mon_att
        self.spd = global_parameters.MON_RUN_SPEED_PPS * (global_parameters.game_level+1)

    def camera_update(self, camera_x, camera_y):
        self.x += camera_x
        self.y += camera_y


#item class
class item:

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
        self.img.draw(self.x, self.y, global_parameters.item_size, global_parameters.item_size)

    def camera_update(self, camera_x, camera_y):
        self.x += camera_x
        self.y += camera_y

    def get_bb(self):
        return self.x - item.size_x/2, self.y - item.size_y/2, self.x + item.size_x/2, self.y + item.size_y/2

#game state에 있는 변수값 여기서 type 따져서 바로 바꿔줘



#bullet class
class bullet:
    size_x, size_y = None, None
    img = None

    def __init__(self, event_x, event_y):
        self.x, self.y = global_parameters.width/2, global_parameters.height/2
        bullet.size_x, bullet.size_y = global_parameters.item_size, global_parameters.item_size
        self.angle = math.atan2((global_parameters.height/2 - event_y) , (global_parameters.width/2 - event_x))
        self.update_angle = (global_parameters.height/2 - event_y) / (global_parameters.width/2 - event_x)
        self.update_pos = event_y - (event_x * self.update_angle)
        if event_x <= global_parameters.width/2:
            self.dir = -1
        elif event_x > global_parameters.width/2:
            self.dir = 1

        if bullet.img == None:
           bullet.img = load_image('bullet.png')

    def update(self, frame_time):
        self.x += self.dir * frame_time * global_parameters.RUN_SPEED_PPS * 2
        self.y = self.x * self.update_angle + self.update_pos
        pass

    def camera_update(self, camera_x, camera_y):
        self.x += camera_x
        self.y += camera_y

    def draw(self):
        self.img.rotate_draw(self.angle, self.x, self.y, self.size_x, self.size_y)

    def get_bb(self):
        return self.x - item.size_x/2, self.y - item.size_y/2, self.x + item.size_x/2, self.y + item.size_y/2