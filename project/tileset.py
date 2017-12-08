__author__ = 'dustinlee'

import json

from pico2d import *

class TileSet:

    def __init__(self):
        self.firstgid = 0

    def load(self, file_name):
        f = open(file_name)
        data = json.load(f)
        f.close()
        self.__dict__.update(data)

        for i in range(self.tilecount):
            col, row = i % self.columns, i // self.columns
            left = col * self.tilewidth

        pass

class TileMap:
    def __init__(self):
        self.firstgid = 0

    def load(self, name):
        f = open(name)
        info = json.load(f)
        f.close()
        self.__dict__.update(info)

        self.data = self.layers[0]['data']
        pass



def load_tile_set(file_name):
    tile_set = TileSet()
    tile_set.load(file_name)

    return tile_set
    pass

if __name__ =='__main__':
    open_canvas(800, 600)

    tile_set = load_tile_set('desert_tileset.json')

    for i in range(tile_set.tilecount):
        col = i % tile_set.columns
        row = i // tile_set.columns
        tile_set.tile_images[i].draw_to_origin(col * tile_set.tilewidth,
                                               row * tile_set.tileheight)

    update_canvas()
    delay(5)
    close_canvas()
    pass
