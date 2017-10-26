import global_parameters
from pico2d import *

class button:
    button_img = None
    m_x, m_y = 0, 0
    s_x, s_y = 0, 0

    mouse_on = False

    def __init__(self, name, x_local, y_local, x_size, y_size):
        if self.button_img == None:
            self.button_img = load_image(name)
        m_x = x_local, m_y = y_local
        s_x = x_size, s_y = y_size

    def draw(self):
        self.button_img.draw(self, self.m_x, self.m_y
                             , self.m_x - self.s_x, self.m_y - self.s_y)

    def click(self, mouse_x, mouse_y):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT: #LBUTTON CLICK
                if(self.m_x - self.s_x <= event.x and event.x <= self.m_x + self.s_x  #COLLISION
                   and self.m_y - self.s_y <= event.y and event.y <= self.m_y + self.s_y):
                    mouse_on = True
