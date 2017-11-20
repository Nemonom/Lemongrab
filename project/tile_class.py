import global_parameters
from pico2d import *

class tile:
    size_x, size_y = global_parameters.tile_size_x, global_parameters.tile_size_y
    wall_img = None
    road_img = None
    def __init__(self, state, x_local, y_local):
        self.state = state
        self.m_x = x_local
        self.m_y = y_local
        if tile.wall_img == None:
            tile.wall_img = load_image('lemon.png')

    def draw(self):
        if self.if_camera():
            if self.state == 1:
                tile.wall_img.draw(self.m_x, self.m_y
                              , tile.size_x, tile.size_y)
                draw_rectangle(self.m_x - global_parameters.tile_size_x/2, self.m_y - global_parameters.tile_size_y/2
                               , self.m_x + global_parameters.tile_size_x/2, self.m_y + global_parameters.tile_size_y/2)
        pass

    def update(self, camera_x, camera_y):
        self.m_x += camera_x
        self.m_y += camera_y
        pass

    def if_camera(self):
        if 0 <= self.m_x + global_parameters.tile_size_y/2 \
                and self.m_x - global_parameters.tile_size_y/2 <= global_parameters.width \
                and 0 <= self.m_y + global_parameters.tile_size_y/2 \
                and self.m_y - global_parameters.tile_size_y/2 <= global_parameters.height:
            return True
