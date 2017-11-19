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

    def draw(self):
        self.img.rotate_draw(self.angle, global_parameters.width/2, global_parameters.height/2
                             , self.size_x, self.size_y)

    def get_angle(self, event_x, event_y):
        self.angle = math.atan2((global_parameters.height/2 - event_y) , (global_parameters.width/2 - event_x))
        pass

    def control_hp(self, what, num):
        if what == '-':
            self.hp -= num
            self.hp = max(0, self.hp)
        elif what == '+':
            self.hp += num
            self.hp = min(100, self.hp)

    def control_mp(self, what, num):
        if what == '-':
            self.mp -= num
            self.mp = max(0, self.hp)
        elif what == '+':
            self.mp += num
            self.mp = min(100, self.mp)

    def increase_hp(self, num):
        self.hp+=num

    def return_hp(self):
        return self.hp

    def return_mp(self):
        return self.mp

    def get_bb(self):
        return global_parameters.width/2 - self.size_x / 2, global_parameters.height/2 - self.size_y / 2\
            , global_parameters.width/2 + self.size_x / 2, global_parameters.height/2 + self.size_y / 2


#enemy class
class enemy:
    size_x, size_y = None, None
    img = None
    RELAX, CHASE, ATTACK = 0, 1, 2

    def __init__(self, x, y):
        if enemy.img == None:
            img = load_image('enemy.png')
        enemy.size_x, enemy.size_y = global_parameters.mon_size_x, global_parameters.mon_size_y
        self.dir_x, self.dir_y = 0, 0
        self.m_x, self.m_y = x, y
        self.hp = global_parameters.mon_hp
        self.att = global_parameters.mon_att
        self.spd = global_parameters.MON_RUN_SPEED_PPS * (global_parameters.game_level+1)

    def camera_update(self, camera_x, camera_y):
        self.m_x += camera_x
        self.m_y += camera_y


    def if_camera(self):
        if 0 <= self.m_x + enemy.size_x / 2 \
                and self.m_x - enemy.size_x / 2 <= global_parameters.width \
                and 0 <= self.m_y + enemy.size_y / 2 \
                and 0 <= self.m_y + enemy.size_y / 2 <= global_parameters.height:
            return True

#item class
class item:

    def __init__(self, what, x, y):
        self.type = what
        self.m_x, self.m_y = x, y
        if what == 0:
            self.img = load_image('lemon.png')
        elif what == 1:
            self.img = load_image('hp.png')
        elif what == 2:
            self.img = load_image('mp.png')
        elif what == 3:
            self.img = load_image('money.png')

    def return_type(self):
        return self.type

    def draw(self):
        if self.if_camera():
            self.img.draw(self.m_x, self.m_y, global_parameters.item_size, global_parameters.item_size)

    def camera_update(self, camera_x, camera_y):
        self.m_x += camera_x
        self.m_y += camera_y

    def get_bb(self):
        return self.m_x - global_parameters.item_size/2, self.m_y - global_parameters.item_size/2\
            , self.m_x + global_parameters.item_size/2, self.m_y + global_parameters.item_size/2

    def if_camera(self):
        if 0 <= self.m_x + global_parameters.item_size / 2 \
                and self.m_x - global_parameters.item_size / 2 <= global_parameters.width \
                and 0 <= self.m_y + global_parameters.item_size / 2 \
                and 0 <= self.m_y + global_parameters.item_size / 2 <= global_parameters.height:
            return True

#bullet class
class bullet:
    img = None

    def __init__(self, event_x, event_y):
        self.x, self.y = global_parameters.width/2, global_parameters.height/2
        self.size_x, self.size_y = global_parameters.item_size, global_parameters.item_size
        self.angle = math.atan2((event_y - global_parameters.height/2) , ( event_x - global_parameters.width/2))


        if bullet.img == None:
           bullet.img = load_image('bullet.png')

    def update(self, frame_time):
        self.x += math.cos(self.angle) * frame_time * global_parameters.RUN_SPEED_PPS * 2
        self.y += math.sin(self.angle) * frame_time * global_parameters.RUN_SPEED_PPS * 2
        pass

    def camera_update(self, camera_x, camera_y):
        self.x += camera_x
        self.y += camera_y

    def draw(self):
        self.img.rotate_draw(self.angle, self.x, self.y, self.size_x, self.size_y)

    def get_bb(self):
        return self.x - self.size_x/2, self.y - self.size_y/2, self.x + self.size_x/2, self.y + self.size_y/2