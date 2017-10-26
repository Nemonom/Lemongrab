import  global_parameters
import random
from pico2d import *


class game_object:
    def __init__(self, name, x, y, w, h):
        self.name = name