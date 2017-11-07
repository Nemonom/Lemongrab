import global_parameters
from pico2d import *


class camera:
    move_x = 0
    move_y = 0

    STOP, LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3, 4

    hor_state = STOP
    ver_state = STOP

    def __init__(self):
        camera.move_x, camera_move_y = 0, 0
        pass

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if self.hor_state in (self.STOP, self.RIGHT):
                self.hor_state = self.LEFT
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            if self.hor_state in (self.STOP, self.LEFT):
                self.hor_state = self.RIGHT
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            if self.hor_state in (self.LEFT,):
                self.hor_state = self.STOP
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_d):
            if self.hor_state in (self.RIGHT,):
                self.hor_state = self.STOP

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
            if self.ver_state in (self.STOP, self.DOWN):
                self.ver_state = self.UP
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
            if self.ver_state in (self.STOP, self.UP):
                self.ver_state = self.DOWN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_w):
            if self.ver_state in (self.UP,):
                self.ver_state = self.STOP
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_s):
            if self.ver_state in (self.DOWN,):
                self.ver_state = self.STOP
    pass


    def update(self):
        if self.hor_state == self.RIGHT:
            camera.move_x = -1
        elif self.hor_state == self.LEFT:
            camera.move_x = +1
        elif self.hor_state == self.STOP:
            camera.move_x = 0

        if self.ver_state == self.UP:
            camera.move_y = -1
        elif self.ver_state == self.DOWN:
            camera.move_y = +1
        elif self.ver_state == self.STOP:
            camera.move_y = 0
    pass

    def return_x(self):
        return camera.move_x
    def return_y(self):
        return camera.move_y
