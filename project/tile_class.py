import global_parameters
from pico2d import *

class back:
    img = None
    def __init__(self):
        self.m_x = 2560
        self.m_y = 3200
        if back.img == None:
            back.img = load_image('map.png')

    def draw(self):
        back.img.draw(self.m_x, self.m_y)
        pass

    def update(self, camera_x, camera_y):
        self.m_x += camera_x
        self.m_y += camera_y
        print(self.m_x)
        print(self.m_y)
        pass



class tile:
    size_x, size_y = global_parameters.tile_size_x, global_parameters.tile_size_y

    def __init__(self, state, x_local, y_local):
        self.state = state
        self.m_x = x_local
        self.m_y = y_local


    def draw(self):
        if self.in_camera_range():
            draw_rectangle(*self.get_bb())
        pass

    def update(self, camera_x, camera_y):
        self.m_x += camera_x
        self.m_y += camera_y
        pass

    def in_camera_range(self):
        if 0 <= self.m_x + tile.size_y/2 \
                and self.m_x - tile.size_y/2 <= global_parameters.width \
                and 0 <= self.m_y + tile.size_y/2 \
                and self.m_y - tile.size_y/2 <= global_parameters.height:
            return True


    def get_bb(self):
        return self.m_x - tile.size_y\
            , self.m_y - tile.size_y\
            , self.m_x + tile.size_y\
            , self.m_y + tile.size_y