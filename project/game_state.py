import global_parameters
import game_framework
import main_state
import mouse_pointer
import button_class

from pico2d import *


name = "game_state"
option_but = None
width = global_parameters.width
height = global_parameters.height

def enter():
    global main_pointer
    global option_but

    main_pointer = mouse_pointer.pointer()
    option_but = button_class.button('option_button.png', 960, 670, 25, 25)


def exit():
    global main_pointer
    global option_but

    del(main_pointer)
    del(option_but)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            option_but.mousemove_on(event.x, 700 - event.y)

        if option_but.get_mouse_on() == True and (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            game_framework.change_state(main_state)



def draw():
    clear_canvas()
    hide_cursor()
    main_pointer.draw(1)
    option_but.draw()
    update_canvas()




def update():
    main_pointer.update()

    pass


def pause():
    pass


def resume():
    pass






