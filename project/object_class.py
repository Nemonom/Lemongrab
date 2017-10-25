import random
import json
import os

from pico2d import *


class tile:
    def __init__(self):
        global tile_image
        self.tile_image = load_image('grass.png')

class game_object:
    def __init__(self, name, x, y, w, h):
        self.name = name