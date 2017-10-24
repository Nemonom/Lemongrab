import game_framework
from pico2d import *


name = "main_state"
image = None


def enter():
    global background
    background = load_image('main.png')


def exit():
    global background
    del(background)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def draw():
    clear_canvas()
    background.draw(500, 350)
    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass






