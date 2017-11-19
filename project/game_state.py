from pico2d import *

import button_class
import camera_class
import game_framework
import global_parameters
import main_state
import mouse_pointer
import tile_class
import object_class

name = "game_state"
option_but = None
width = global_parameters.width
height = global_parameters.height

goal_lemon = 0
collect_lemon = 0
lemon_img = None
b_lemon_img = None

money_img = None
font = None
collect_money = 0

normal_state_img = None
attack_state_img = None
hp_bar_img = None
mp_bar_img = None

player = None
player_get_attack = False
get_attack_time_cnt = 0

bullets = None

items = None


camera = None
test = None



def enter():
    global main_pointer
    global test
    global camera
    global player
    global bullets
    global items

    camera = camera_class.camera()
    test = tile_class.tile(1, 100, 100)
    UI_init()

    main_pointer = mouse_pointer.pointer()

    player = object_class.player()
    bullets = []
    items = []

def exit():
    global main_pointer
    global test
    global camera
    global player
    global bullets
    global items
    UI_exit()

    del main_pointer
    del test
    del camera
    del player
    del bullets
    del items

def handle_events():
    global camera
    global option_but
    global bullets

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type in (SDL_MOUSEBUTTONUP, SDL_MOUSEBUTTONDOWN, SDL_MOUSEMOTION):
            main_pointer.update(event.x, 700 - event.y)
            player.get_angle(event.x, 700 - event.y)
            option_but.mousemove_on(event.x, 700 - event.y)

            if event.button == SDL_BUTTON_LEFT:
                if option_but.get_mouse_on():
                    game_framework.change_state(main_state)
                else:
                    if event.type == SDL_MOUSEBUTTONDOWN:
                        bullet = object_class.bullet(event.x, 700 - event.y)
                        bullets.append(bullet)

        else:
            camera.handle_event(event)
            #치트키
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_F1:
                    player.control_hp('-', 10)
                elif event.key == SDLK_F2:
                    player.control_mp('-', 10)
                elif event.key == SDLK_F3:
                    player.control_hp('+', 10)
                elif event.key == SDLK_F4:
                    player.control_mp('+', 10)



def draw():
    global test
    global main_pointer
    global option_but
    global player
    global bullets

    clear_canvas()
    hide_cursor()
    player.draw()
    for bullet in bullets:
        bullet.draw()
    test.draw()
    UI_draw()
    option_but.draw()
    main_pointer.draw(1)
    update_canvas()
    pass

def update():
    global camera
    global test
    global bullets

    frame_time = get_frame_time()

    camera.update(frame_time)
    test.update(camera.return_x(), camera.return_y())

    for bullet in bullets:
        bullet.camera_update(camera.return_x(), camera.return_y())
        bullet.update(frame_time)

    player_get_attack_time(frame_time)
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
    global font
    global normal_state_img
    global attack_state_img
    global hp_bar_img
    global mp_bar_img

    option_but = button_class.button('option_button.png', 970, 665, 25, 25)

    collect_lemon = 0
    if global_parameters.game_level == 0:
        goal_lemon = 3
    elif global_parameters.game_level == 1:
        goal_lemon = 5

    lemon_img = load_image('lemon.png')
    b_lemon_img = load_image('b_lemon.png')
    money_img = load_image('money.png')
    if font == None:
        font = load_font('Alice_in_Wonderland.ttf', 20)

    normal_state_img = load_image('normal_state.png')
    attack_state_img = load_image('attack_state.png')
    hp_bar_img = load_image('hp_bar.png')
    mp_bar_img = load_image('mp_bar.png')
    pass

def UI_draw():
    global goal_lemon
    global lemon_img
    global b_lemon_img
    global money_img
    global font
    global collect_money
    global normal_state_img
    global attack_state_img
    global hp_bar_img
    global mp_bar_img

    for i in range(goal_lemon):
        if i < collect_lemon:
            lemon_img.draw(25 + (i * 40), 25
                           , global_parameters.ect_size_x, global_parameters.ect_size_x)
        else:
            b_lemon_img.draw(25 + (i * 40), 25
                            , global_parameters.ect_size_x, global_parameters.ect_size_x)

    if player_get_attack:
        attack_state_img.draw(45, 650, global_parameters.icon_size_x, global_parameters.icon_size_y)
    else:
        normal_state_img.draw(45, 650, global_parameters.icon_size_x, global_parameters.icon_size_y)
    money_img.draw(100, 590, global_parameters.ect_size_x, global_parameters.ect_size_y)
    font.draw(120, 590, 'X %d' % collect_money, (50, 50, 50))
    mp_bar_img.draw(80+player.return_mp(), 630, player.return_mp()*2, global_parameters.icon_size_y/3)
    hp_bar_img.draw(80+player.return_hp(), 660, player.return_hp()*2, global_parameters.icon_size_y/3)

    pass

def UI_exit():
    global option_but
    global lemon_img
    global b_lemon_img
    global money_img
    global font
    global normal_state_img
    global attack_state_img
    global hp_bar_img
    global mp_bar_img


    del option_but
    del lemon_img
    del b_lemon_img
    del money_img
    del font
    del normal_state_img
    del attack_state_img
    del hp_bar_img
    del mp_bar_img
    pass






current_time = 0.0


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def player_get_attack_time(frame_time):
    global get_attack_time_cnt
    global player_get_attack

    if player_get_attack:
        get_attack_time_cnt += frame_time

        if get_attack_time_cnt >= 1:
            get_attack_time_cnt = 0
            player_get_attack = False

    pass