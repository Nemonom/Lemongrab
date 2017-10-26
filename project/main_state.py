import global_parameters
import game_framework
import mouse_pointer
from pico2d import *


name = "main_state"
image = None
main_pointer = None
width = global_parameters.width
height = global_parameters.height

def enter():
    global background
    global main_pointer
    main_pointer = mouse_pointer.pointer()
    main_pointer.__init__()
    background = load_image('main.png')

def exit():
    global background
    global main_pointer
    del(background)
    del(main_pointer)

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
    hide_cursor()
    background.draw(width/2, height/2)
    main_pointer.draw(0)
    update_canvas()






def update():
    main_pointer.update()
    pass


def pause():
    pass


def resume():
    pass






