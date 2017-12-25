from pico2d import *
import random
import button_class
import camera_class
import game_framework
import global_parameters
import main_state
import mouse_pointer
import tile_class
import object_class
import pause_state

from tileset import TileSet as wholetile
from tileset import TileMap as tilemap

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

map_img = None

clear_img = None
game_clear = False

over_img = None
game_over = False

logo_time = 0

f_bullet_time = 0
b_bullet_time = False

space_down = False

game_bgm = None
bullet_bgm = None

def load_tile_set(file_name):
    tile_set = wholetile()
    tile_set.load(file_name)
    return tile_set
    pass

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
    global map_img
    global clear_img
    global game_clear
    global over_img
    global game_over

    global_parameters.global_bgm.stop_bgm('title')
    global_parameters.global_bgm.play_bgm('game')

    game_clear = False
    clear_img = load_image('clear.png')

    game_over = False
    over_img = load_image('over.png')

    real_back = load_image('game_back.png')
    UI_init()
    camera = camera_class.camera()
    main_pointer = mouse_pointer.pointer()
    player = object_class.player()
    bullets = []

    tiles = []
    jsontile = load_tile_set('desert_tileset.json')
    mapdata = tilemap()
    mapdata.load('map.json')

    for i in range(jsontile.tilecount):
        col = i % jsontile.columns
        row = i // jsontile.columns
        row = 100 - row - 1
        put_tile = tile_class.tile(mapdata.data[i]
                                   , col * jsontile.tilewidth + jsontile.tilewidth/2 - 500
                                   , row * jsontile.tileheight + jsontile.tileheight/2)

        tiles.append(put_tile)

    enemys = []

    item_cnt = 0
    while item_cnt < (goal_lemon *2):
        put_ok = 0
        enemy = object_class.enemy(random.randint(20, 2000), random.randint(20, 2000))
        for tile in tiles:
            if collision(enemy, tile) and tile.state != 63:
                put_ok = 5

        if put_ok != 5:
            enemys.append(enemy)
            item_cnt += 1



    items = []

    item_cnt = 0
    while item_cnt < goal_lemon:
       put_ok = 0
       #5100 6370
       lemon = object_class.item(0, random.randint(20, 2000), random.randint(20, 2000))
       for tile in tiles:
           if collision(lemon, tile) and tile.state != 63:
               put_ok = 5

       if put_ok != 5:
           items.append(lemon)
           item_cnt += 1

    item_cnt = 0
    while item_cnt < (global_parameters.game_level + 1) * 10:
        put_ok = 0

        potion_h = object_class.item(1, random.randint(20, 5100), random.randint(20, 6370))
        for tile in tiles:
            if collision(potion_h, tile) and tile.state != 63:
                put_ok = 5

        if put_ok != 5:
            items.append(potion_h)
            item_cnt += 1

    item_cnt = 0
    while item_cnt < (global_parameters.game_level + 1) * 10:
        put_ok = 0

        potion_m = object_class.item(2, random.randint(20, 5100), random.randint(20, 6370))
        for tile in tiles:
            if collision(potion_m, tile) and tile.state != 63:
                put_ok = 5

        if put_ok != 5:
            items.append(potion_m)
            item_cnt += 1


    map_img = tile_class.back()

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
    global map_img
    global clear_img

    global_parameters.global_bgm.stop_bgm('game')
    global_parameters.global_bgm.play_bgm('title')
    global_parameters.my_money += collect_money
    collect_money = 0

    UI_exit()

    del clear_img
    del map_img
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
    global b_bullet_time
    global space_down
    global player


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
                    game_framework.push_state(pause_state)
                else:
                    if event.type == SDL_MOUSEBUTTONDOWN:
                        if b_bullet_time == False:
                            if player.mp >= 2:
                                bullet = object_class.bullet(event.x, 700 - event.y)
                                bullets.append(bullet)
                                global_parameters.global_snd.play_snd('bullet')
                                player.mp -= 2
                                b_bullet_time = True


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
                elif event.key == SDLK_SPACE:
                    space_down = True
            if event.type == SDL_KEYUP:
                if event.key == SDLK_SPACE:
                    space_down = False

def draw():
    clear_canvas()
    hide_cursor()

    game_draw()

    update_canvas()
    pass

def game_draw():
    global real_back
    global tiles
    global main_pointer
    global option_but
    global player
    global bullets
    global items
    global enemys
    global jsontile
    global map_img
    global game_clear

    real_back.draw(500, 350, 1000, 700)
    map_img.draw()

    player.draw()
    for item in items:
        item.draw()
    for enemy in enemys:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    UI_draw()
    option_but.draw()
    main_pointer.draw(1)

    if game_clear:
        clear_img.draw(500, 350, 1000, 700)
    elif game_over:
        over_img.draw(500, 350, 1000, 700)

def update(frame_time):
    global camera
    global tiles
    global bullets
    global items
    global player
    global collect_lemon
    global collect_money
    global enemys
    global player_hurt
    global map_img
    global clear_img
    global game_clear
    global f_bullet_time
    global b_bullet_time
    global space_down
    global game_over
    global logo_time

    player.control_mp('+', 0.01)

    if b_bullet_time:
        f_bullet_time += frame_time
        if f_bullet_time >= 0.3:
            b_bullet_time = False
            f_bullet_time = 0

    if space_down:
        player.mp -= 0.1
        if player.mp < 0:
            space_down = False

    if game_over:
        if (logo_time > 3):
            logo_time = 0
            game_framework.change_state((main_state))
        delay(0.01)
        logo_time += 0.01

    elif game_clear:
        if (logo_time > 3):
            logo_time = 0
            game_framework.change_state((main_state))
        delay(0.01)
        logo_time += 0.01

    else:
        inter_w, inter_h = 0, 0
        i_collision = False
        player_hurt = False

        camera.update(frame_time, space_down)


        for tile in tiles:
            tile.update(camera.move_x, camera.move_y)
            if tile.in_camera_range() and collision(player, tile) and tile.state != 63:
                inter_w, inter_h = intersect_pos(tile, player)
                i_collision = True
                pass

        for item in items:
            item.camera_update(camera.move_x, camera.move_y)
            if item.in_camera_range(): # 카메라 안에 있는 아이템 충돌체크
                if collision(player, item):
                    global_parameters.global_snd.play_snd('eat')
                    if item.return_type() == 0:
                        collect_lemon += 1
                    elif item.return_type() == 1:
                        player.control_hp('+', global_parameters.hp_item+global_parameters.shop_potion_level*2)
                    elif item.return_type() == 2:
                        player.control_mp('+', global_parameters.mp_item+global_parameters.shop_potion_level*2)
                    elif item.return_type() == 3:
                        collect_money += 100

                    items.remove(item)

        for enemy in enemys:
            if enemy.in_camera_range():
                enemy.state = enemy.CHASE
                if collision(enemy, player):
                    enemy.state = enemy.ATTACK
                    player.control_hp('-', 0.1)
                    player_hurt = True
            else:
                enemy.state = enemy.RELAX
            enemy.update(frame_time, global_parameters.width/2, global_parameters.height/2)
            enemy.camera_update(camera.move_x, camera.move_y)

        for bullet in bullets:
            bullet.update(frame_time)
            bullet.camera_update(camera.move_x, camera.move_y)

            for enemy in enemys:
                if enemy.in_camera_range():
                    if collision(bullet, enemy):
                        enemy.hp -= 5 + global_parameters.shop_att_level * 3
                        if enemy.hp < 0:
                            enemys.remove(enemy)
                            item = object_class.item(3, enemy.m_x, enemy.m_y)
                            items.append(item)
                        bullets.remove(bullet)
                        break


            for tile in tiles:
                if tile.in_camera_range() and collision(bullet, tile) and tile.state != 63:
                    bullets.remove(bullet)
                    break

            if bullet.in_camera_range() == False:
                bullets.remove(bullet)


        map_img.update(camera.move_x, camera.move_y)

        if i_collision:
            map_img.update(inter_w, inter_h)
            for tile in tiles:
                tile.update(inter_w, inter_h)
            for item in items:
                item.camera_update(inter_w, inter_h)
            for bullet in bullets:
                bullet.camera_update(inter_w, inter_h)
            for enemy in enemys:
                enemy.camera_update(inter_w, inter_h)

        if player.return_hp() <= 0:
            delay(0.05)
            game_over = True
            global_parameters.global_snd.play_snd('over')

        if collect_lemon == goal_lemon:
            delay(0.05)
            game_clear = True
            global_parameters.global_snd.play_snd('yell')

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