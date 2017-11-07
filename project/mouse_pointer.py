import global_parameters
from pico2d import *

class pointer:
    def __init__(self):
        self.image1 = load_image('lemon.png')
        self.image2 = load_image('lemon.png')

        self.x, self.y = 0, 0

    def update(self, event_x, event_y):
        self.x, self.y = event_x, event_y

    def draw(self, a):
        if a == 0:
            self.image1.draw(self.x, self.y
                            , global_parameters.mouse_pointer_size, global_parameters.mouse_pointer_size)
        elif a == 1:
            self.image2.draw(self.x, self.y
                            , global_parameters.mouse_pointer_size, global_parameters.mouse_pointer_size)