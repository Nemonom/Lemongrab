import global_parameters
from pico2d import *

class button:
    def __init__(self, name, x_local, y_local, x_size, y_size):
        self.button_img = load_image(name)
        self.m_x = x_local
        self.m_y = y_local
        self.s_x = x_size
        self.s_y = y_size
        self.mouse_on = False

    def draw(self):
        if self.mouse_on:
            self.button_img.draw(self.m_x, self.m_y
                                 , self.s_x * 2 +10, self.s_y * 2+10)
        else:
            self.button_img.draw(self.m_x, self.m_y
                             , self.s_x * 2, self.s_y * 2)




    def mousemove_on(self, mouse_x, mouse_y):
        if(self.m_x - self.s_x <= mouse_x and mouse_x <= self.m_x + self.s_x and self.m_y - self.s_y <= mouse_y and mouse_y <= self.m_y + self.s_y):
            self.mouse_on = True
        else:
            self.mouse_on = False

    def get_mouse_on(self):
        return self.mouse_on