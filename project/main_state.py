import global_parameters
import game_framework
import help_state
import level_state
import mouse_pointer
import button_class

from pico2d import *


name = "main_state"
image = None
main_pointer = None
exit_but = None
start_but = None
help_but = None
width = global_parameters.width
height = global_parameters.height

def enter():
    global background
    global main_pointer
    global exit_but
    global start_but
    global help_but

    background = load_image('main.png')
    main_pointer = mouse_pointer.pointer()
    exit_but = button_class.button('exit_button.png', 900, 50, 100, 50)
    start_but = button_class.button('start_button.png', 500, 50, 100, 50)
    help_but = button_class.button('help_button.png', 700, 50, 100, 50)


def exit():
    global background
    global main_pointer
    global exit_but
    global start_but
    global help_but

    del(background)
    del(main_pointer)
    del(exit_but)
    del(start_but)
    del(help_but)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            start_but.mousemove_on(event.x, 700 - event.y)
            help_but.mousemove_on(event.x, 700 - event.y)
            exit_but.mousemove_on(event.x, 700 - event.y)

        if ((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)):
            if start_but.get_mouse_on():
                game_framework.change_state(level_state)
            elif help_but.get_mouse_on():
                game_framework.change_state(help_state)
            elif exit_but.get_mouse_on():
                game_framework.quit()

        elif event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def draw():
    clear_canvas()
    hide_cursor()
    background.draw(width/2, height/2)
    main_pointer.draw(0)
    exit_but.draw()
    start_but.draw()
    help_but.draw()
    update_canvas()






def update():
    main_pointer.update()

    pass


def pause():
    pass


def resume():
    pass






