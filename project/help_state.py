import global_parameters
import game_framework
import main_state
import mouse_pointer
import button_class

from pico2d import *


name = "help_state"
image = None
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
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            exit_but.mousemove_on(event.x, 700 - event.y)

        if exit_but.get_mouse_on() == True and (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            game_framework.change_state(main_state)

        if event.type == SDL_QUIT:
            game_framework.quit()


def draw():
    clear_canvas()
    hide_cursor()
    background.draw(width/2, height/2)
    main_pointer.draw(0)
    exit_but.draw()
    update_canvas()






def update():
    main_pointer.update()
    pass


def pause():
    pass


def resume():
    pass

