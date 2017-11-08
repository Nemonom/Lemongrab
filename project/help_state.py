import global_parameters
import game_framework
import main_state
import mouse_pointer
import button_class

from pico2d import *


name = "help_state"
background = None
exit_but = None
width = global_parameters.width
height = global_parameters.height

def enter():
    global background
    global main_pointer
    global exit_but

    background = load_image('help.png')
    main_pointer = mouse_pointer.pointer()
    exit_but = button_class.button('exit_button2.png', 950, 660, 80, 40)

def exit():
    global background
    global main_pointer
    global exit_but

    del(background)
    del(main_pointer)
    del(exit_but)

def handle_events():
    global exit_but

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type in (SDL_MOUSEBUTTONUP, SDL_MOUSEBUTTONDOWN, SDL_MOUSEMOTION):
            main_pointer.update(event.x, 700 - event.y)
            exit_but.mousemove_on(event.x, 700 - event.y)

            if event.button == SDL_BUTTON_LEFT:
                if exit_but.get_mouse_on():
                    game_framework.change_state(main_state)



def draw():
    global background
    global main_pointer
    global exit_but
    clear_canvas()
    hide_cursor()
    background.draw(width/2, height/2)
    exit_but.draw()
    main_pointer.draw(0)
    update_canvas()


def update():

    pass


def pause():
    pass


def resume():
    pass

