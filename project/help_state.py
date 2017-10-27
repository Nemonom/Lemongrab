import global_parameters
import game_framework
import mouse_pointer
import button_class

from pico2d import *


name = "help_state"
image = None
main_pointer = None
exit_button = None
width = global_parameters.width
height = global_parameters.height

def enter():
    global background
    global main_pointer
    global exit_button

    background = load_image('help.png')
    main_pointer = mouse_pointer.pointer()
    exit_button = button_class.button('exit_button2.png', 950, 650, 25, 25)

def exit():
    global background
    global main_pointer
    global exit_button

    del(background)
    del(main_pointer)
    del(exit_button)

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
    main_pointer.draw()
    exit_button.draw()
    update_canvas()






def update():
    main_pointer.update()
    pass


def pause():
    pass


def resume():
    pass

