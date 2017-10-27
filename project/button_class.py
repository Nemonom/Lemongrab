import global_parameters
from pico2d import *

class button:
    button_img = None
    m_x = 0
    m_y = 0
    s_x = 0
    s_y = 0

    mouse_on = False

    def __init__(self, name, x_local, y_local, x_size, y_size):
        if button.button_img == None:
            button.button_img = load_image(name)
        self.m_x = x_local
        self.m_y = y_local
        self.s_x = x_size
        self.s_y = y_size

    def draw(self):
        self.button_img.draw(self.m_x, self.m_y
                             , self.s_x * 2, self.s_y * 2)

        if self.mouse_on:
            self.button_img.draw(500, 500, 500, 500)

    def mousemove_on(self, mouse_x, mouse_y):
        if(self.m_x - self.s_x <= mouse_x and mouse_x <= self.m_x + self.s_x and self.m_y - self.s_y <= mouse_y and mouse_y <= self.m_y + self.s_y):
            self.mouse_on = True
        else:
            self.mouse_on = False

    def get_mouse_on(self):
        return self.mouse_on