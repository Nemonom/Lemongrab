from pico2d import *

class pointer:
    def __init__(self):
        self.x, self.y = 500, 350
        self.image = load_image('lemon.png')

    def update(self):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                self.x, self.y = event.x, 700 - event.y

    def draw(self):
        self.image.draw(self.x, self.y, 30, 30)
