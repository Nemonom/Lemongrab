import global_parameters
import game_framework
import main_state
import mouse_pointer
import button_class
import tile_class
import camera_class

from pico2d import *


name = "game_state"
option_but = None
width = global_parameters.width
height = global_parameters.height
player_hp, player_mp = 0, 0
goal_lemon = 0

camera = None

test = None


def enter():
    global main_pointer
    global test
    global camera

    camera = camera_class.camera()
    test = tile_class.tile("lemon.png", 1, 500, 500)
    UI_init()

    main_pointer = mouse_pointer.pointer()


def exit():
    global main_pointer
    global option_but
    global test
    global camera

    del(main_pointer)
    del(option_but)
    del(test)
    del(camera)

def handle_events():
    global camera
    global option_but

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type in (SDL_MOUSEBUTTONUP, SDL_MOUSEBUTTONDOWN, SDL_MOUSEMOTION):
            main_pointer.update(event.x, 700 - event.y)
            option_but.mousemove_on(event.x, 700 - event.y)

            if event.button == SDL_BUTTON_LEFT:
                if option_but.get_mouse_on():
                    game_framework.change_state(main_state)

        else:
            camera.handle_event(event)


def draw():
    global test
    global main_pointer
    global option_but
    clear_canvas()
    hide_cursor()
    main_pointer.draw(1)
    option_but.draw()
    test.draw()
    update_canvas()
    pass

def update():
    global camera
    global test

    camera.update()
    test.update(camera.return_x(), camera.return_y())
    pass


def pause():
    pass


def resume():
    pass



def UI_init():
    global option_but
    global player_hp, player_mp
    global goal_lemon

    option_but = button_class.button('option_button.png', 970, 665, 25, 25)

    player_hp = global_parameters.player_hp
    player_mp = global_parameters.player_mp

    if global_parameters.game_level == 0:
        goal_lemon = 3
    elif global_parameters.game_level == 1:
        goal_lemon = 5



    pass

def UI_draw():

    pass

