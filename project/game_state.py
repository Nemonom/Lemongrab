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
goal_lemon = 0
collect_lemon = 0
lemon_img = None
b_lemon_img = None
money_img = None
normal_state_img = None
attack_state_img = None

camera = None

test = None


def enter():
    global main_pointer
    global test
    global camera

    camera = camera_class.camera()
    test = tile_class.tile("lemon.png", 1, 100, 100)
    UI_init()

    main_pointer = mouse_pointer.pointer()


def exit():
    global main_pointer
    global option_but
    global test
    global camera
    global lemon_img
    global b_lemon_img
    global money_img
    global normal_state_img
    global attack_state_img

    del(main_pointer)
    del(option_but)
    del(test)
    del(camera)
    del(lemon_img)
    del(b_lemon_img)
    del money_img
    del normal_state_img
    del attack_state_img

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
    UI_draw()
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
    global collect_lemon
    global goal_lemon
    global lemon_img
    global b_lemon_img
    global money_img
    global normal_state_img
    global attack_state_img

    option_but = button_class.button('option_button.png', 970, 665, 25, 25)

    collect_lemon = 0
    if global_parameters.game_level == 0:
        goal_lemon = 3
    elif global_parameters.game_level == 1:
        goal_lemon = 5

    lemon_img = load_image('lemon.png')
    b_lemon_img = load_image('b_lemon.png')
    money_img = load_image('money.png')
    normal_state_img = load_image('normal_state.png')
    attack_state_img = load_image('attack_state.png')

    pass

def UI_draw():
    global goal_lemon
    global lemon_img
    global b_lemon_img
    global money_img
    global normal_state_img
    global attack_state_img

    for i in range(goal_lemon):
        if i < collect_lemon:
            lemon_img.draw(25 + (i * 40), 25
                           , global_parameters.ect_size_x, global_parameters.ect_size_x)
        else:
            b_lemon_img.draw(25 + (i * 40), 25
                            , global_parameters.ect_size_x, global_parameters.ect_size_x)

    normal_state_img.draw(45, 650, global_parameters.icon_size_x, global_parameters.icon_size_y)
    money_img.draw(100, 580, global_parameters.ect_size_x, global_parameters.ect_size_y)

    pass

