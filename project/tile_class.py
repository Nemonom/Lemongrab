import global_parameters
from pico2d import *

class tile:
    size_x, size_y = global_parameters.tile_size_x, global_parameters.tile_size_y

    def __init__(self, state, x_local, y_local, image):
        self.state = state
        self.m_x = x_local
        self.m_y = y_local
        self.img = image


    def draw(self):
        if self.in_camera_range():
            self.img.draw(self.m_x, self.m_y
                              , tile.size_x, tile.size_y)
            draw_rectangle(self.m_x - tile.size_x, self.m_y - tile.size_y
                           , self.m_x + tile.size_x, self.m_x + tile.size_x)
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
        return self.m_x - tile.size_y/2\
            , self.m_y - tile.size_y/2\
            , self.m_x + tile.size_y/2\
            , self.m_y + tile.size_y/2