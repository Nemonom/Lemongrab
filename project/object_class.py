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
            self.mp = max(0, self.mp)
        elif what == '+':
            self.mp += num
            self.mp = min(100, self.mp)

    def return_hp(self):
        return self.hp

    def return_mp(self):
        return self.mp

    def get_bb(self):
        return global_parameters.width/2 - self.size_x / 4, global_parameters.height/2 - self.size_y / 4\
            , global_parameters.width/2 + self.size_x / 4, global_parameters.height/2 + self.size_y / 4


#enemy class
class enemy:
    size_x, size_y = None, None
    img0, img1, img2 = None, None, None
    RELAX, CHASE, ATTACK = 0, 1, 2

    def __init__(self, x, y):
        if enemy.img0 == None:
            enemy.img0 = load_image('e1.png')
        if enemy.img1 == None:
            enemy.img1 = load_image('e2.png')
        if enemy.img2 == None:
            enemy.img2 = load_image('e3.png')

        enemy.size_x, enemy.size_y = global_parameters.mon_size_x, global_parameters.mon_size_y
        self.m_x, self.m_y = x, y
        self.hp = global_parameters.mon_hp
        self.att = global_parameters.mon_att
        self.spd = global_parameters.MON_RUN_SPEED_PPS * (global_parameters.game_level+1) + random.randint(0, 200)
        self.state = enemy.RELAX
        self.frame =  random.randint(0, 2)

    def camera_update(self, camera_x, camera_y):
        self.m_x += camera_x
        self.m_y += camera_y

    def update(self, frame_time, player_x, player_y):
        self.frame = (self.frame+0.1)%3

        self.angle = math.atan2((-self.m_y + global_parameters.height / 2), (-self.m_x + global_parameters.width / 2))
        if self.state == enemy.RELAX:
            pass
        elif self.state == enemy.CHASE:
            self.m_x += math.cos(self.angle) * frame_time\
                        * global_parameters.MON_RUN_SPEED_PPS * (1 + random.randint(0, global_parameters.game_level*10)/100)

            self.m_y += math.sin(self.angle) * frame_time\
                        * global_parameters.MON_RUN_SPEED_PPS * (1 + random.randint(0, global_parameters.game_level*10)/100)
            pass
        elif self.state == enemy.ATTACK:
            pass


    def in_camera_range(self):
        if 0 <= self.m_x + enemy.size_x / 2 \
                and self.m_x - enemy.size_x / 2 <= global_parameters.width \
                and 0 <= self.m_y + enemy.size_y / 2 \
                and 0 <= self.m_y + enemy.size_y / 2 <= global_parameters.height:
            return True

    def draw(self):
        if self.in_camera_range():
            if self.frame >= 0 and self.frame < 1:
                enemy.img0.rotate_draw(self.angle, self.m_x, self.m_y, enemy.size_x, enemy.size_x)
            elif self.frame >= 1 and self.frame < 2:
                enemy.img1.rotate_draw(self.angle, self.m_x, self.m_y, enemy.size_x, enemy.size_x)
            elif self.frame >= 2 and self.frame < 3:
                enemy.img2.rotate_draw(self.angle, self.m_x, self.m_y, enemy.size_x, enemy.size_x)

    def get_bb(self):
        return self.m_x - enemy.size_x / 2, self.m_y - enemy.size_x / 2 \
            , self.m_x + enemy.size_x / 2, self.m_y + enemy.size_x / 2


#item class
class item:
    img = None
    size_x, size_y = None, None
    def __init__(self, what, x, y):
        self.type = what
        self.m_x, self.m_y = x, y
        item.size_x, item.size_y = global_parameters.item_size, global_parameters.item_size
        if what == 0:
            self.img = load_image('lemon.png')
        elif what == 1:
            self.img = load_image('hp_item.png')
        elif what == 2:
            self.img = load_image('mp_item.png')
        elif what == 3:
            self.img = load_image('money.png')

    def return_type(self):
        return self.type

    def draw(self):
        if self.in_camera_range():
            self.img.draw(self.m_x, self.m_y, item.size_x, item.size_y)

    def camera_update(self, camera_x, camera_y):
        self.m_x += camera_x
        self.m_y += camera_y

    def get_bb(self):
        return self.m_x - item.size_x/2, self.m_y - item.size_x/2\
            , self.m_x + item.size_x/2, self.m_y + item.size_x/2

    def in_camera_range(self):
        if 0 <= self.m_x + item.size_x \
                and self.m_x - item.size_x <= global_parameters.width \
                and 0 <= self.m_y + item.size_x \
                and self.m_y - item.size_x <= global_parameters.height:
            return True

#bullet class
class bullet:
    img = None
    size_x, size_y = None, None

    def __init__(self, event_x, event_y):
        self.x, self.y = global_parameters.width/2, global_parameters.height/2
        bullet.size_x, bullet.size_y = global_parameters.item_size/2, global_parameters.item_size/2
        self.angle = math.atan2((event_y - global_parameters.height/2) , ( event_x - global_parameters.width/2))
        if bullet.img == None:
           bullet.img = load_image('bullet.png')

    def update(self, frame_time):
        self.x += math.cos(self.angle) * frame_time * global_parameters.RUN_SPEED_PPS * 4
        self.y += math.sin(self.angle) * frame_time * global_parameters.RUN_SPEED_PPS * 4
        pass

    def camera_update(self, camera_x, camera_y):
        self.x += camera_x
        self.y += camera_y

    def draw(self):
        self.img.rotate_draw(self.angle, self.x, self.y, bullet.size_x, bullet.size_y)

    def get_bb(self):
        return self.x - bullet.size_x/2, self.y - bullet.size_y/2, self.x + bullet.size_x/2, self.y + bullet.size_y/2

    def in_camera_range(self):
        if 0 <= self.x + bullet.size_x/2 \
                and self.x - bullet.size_x/2 <= global_parameters.width \
                and 0 <= self.y + bullet.size_y/2 \
                and self.y - bullet.size_y/2 <= global_parameters.height:
            return True
