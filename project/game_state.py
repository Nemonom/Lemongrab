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
real_back = None
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
player_hurt = False

#오브젝트 배열
bullets = None
items = None
tiles = None
enemys = None

camera = None
test = None



def enter():
    global real_back
    global main_pointer
    global test
    global camera
    global player
    global bullets
    global items
    global tiles
    global enemys

    real_back = load_image('game_back.png')
    UI_init()
    camera = camera_class.camera()
    main_pointer = mouse_pointer.pointer()
    player = object_class.player()
    bullets = []
    items = [object_class.item(i, 100 * i, 200 * i) for i in range(4)]
    tiles = []
    test = tile_class.tile(1, 100, 100)
    tiles.append(test)
    enemys = []

def exit():
    global real_back
    global main_pointer
    global tiles
    global camera
    global player
    global bullets
    global items
    global collect_money
    global enemys

    global_parameters.my_money += collect_money
    collect_money = 0

    UI_exit()

    del real_back
    del main_pointer
    del tiles
    del camera
    del player
    del bullets
    del items
    del enemys

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
                        if player.mp >= 2:
                            bullet = object_class.bullet(event.x, 700 - event.y)
                            bullets.append(bullet)
                            player.mp -= 2

        else:
            camera.handle_event(event)
            #치트키
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_1:
                    player.control_hp('-', 10)
                elif event.key == SDLK_2:
                    player.control_mp('-', 10)
                elif event.key == SDLK_3:
                    player.control_hp('+', 10)
                elif event.key == SDLK_4:
                    player.control_mp('+', 10)


def draw():
    global real_back
    global tiles
    global main_pointer
    global option_but
    global player
    global bullets
    global items
    global enemys

    clear_canvas()
    hide_cursor()
    real_back.draw(500, 350, 1000, 700)
    player.draw()
    for bullet in bullets:
        bullet.draw()
    for item in items:
        item.draw()
    for tile in tiles:
        tile.draw()
    for enemy in enemys:
        enemy.draw()

    UI_draw()
    option_but.draw()
    main_pointer.draw(1)
    update_canvas()
    pass

def update():
    global camera
    global tiles
    global bullets
    global items
    global player
    global collect_lemon
    global collect_money
    global enemys
    global player_hurt

    inter_w, inter_h = 0, 0
    i_collision = False
    player_hurt = False

    frame_time = get_frame_time()
    camera.update(frame_time)


    for tile in tiles:
        tile.update(camera.move_x, camera.move_y)
        if tile.in_camera_range() and collision(player, tile):
            inter_w, inter_h = intersect_pos(tile, player)
            i_collision = True
            pass

    for item in items:
        item.camera_update(camera.move_x, camera.move_y)
        if item.in_camera_range(): # 카메라 안에 있는 아이템 충돌체크
            if collision(player, item):
                if item.return_type() == 0:
                    collect_lemon += 1
                elif item.return_type() == 1:
                    player.control_hp('+', global_parameters.hp_item)
                elif item.return_type() == 2:
                    player.control_mp('+', global_parameters.mp_item)
                elif item.return_type() == 3:
                    collect_money += 100

                items.remove(item)

    for enemy in enemys:
        if enemy.in_camera_range():
            enemy.state = enemy.CHASE
            if collision(enemy, player):
                enemy.state = enemy.ATTACK
                player_hurt = True
        else:
            enemy.state = enemy.RELAX
        enemy.update(frame_time)
        enemy.camera_update(camera.move_x, camera.move_y)

    for bullet in bullets:
        bullet.update(frame_time)
        bullet.camera_update(camera.move_x, camera.move_y)
        for tile in tiles:
            if collision(bullet, tile):
                bullets.remove(bullet)
        for enemy in enemys:
            if collision(bullet, enemy):
                enemy.hp -= 5



    if i_collision:
        for tile in tiles:
            tile.update(inter_w, inter_h)
        for item in items:
            item.camera_update(inter_w, inter_h)
        for bullet in bullets:
            bullet.camera_update(inter_w, inter_h)
        for enemy in enemys:
            enemy.camera_update(inter_w, inter_h)

    if player.return_hp() <= 0 or collect_lemon == goal_lemon:
        game_framework.change_state(main_state)

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

    if player_hurt:
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

def collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def intersect_pos(a, b):

    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    intersect_top = min(top_a, top_b)
    intersect_bottom = max(bottom_a, bottom_b)
    intersect_right = min(right_a, right_b)
    intersect_left = max(left_a, left_b)

    inter_w = intersect_right - intersect_left
    inter_h = intersect_top - intersect_bottom

    if inter_w > inter_h:
        if top_b>top_a:
           return 0, -inter_h
        else:
            return 0, inter_h
    else:
        if right_b > right_a:
            return -inter_w, 0
        else:
            return inter_w, 0

    pass