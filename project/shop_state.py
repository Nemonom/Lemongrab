import global_parameters
import game_framework
import level_state
import mouse_pointer
import button_class

from pico2d import *


name = "shop_state"
image = None
shop_exit_but = None

width = global_parameters.width
height = global_parameters.height

font = None
att_but = None
potion_but = None

money = None

def enter():
    global background
    global main_pointer
    global shop_exit_but
    global font
    global att_but
    global potion_but
    global money

    money = load_image('money.png')
    background = load_image('level.png')
    main_pointer = mouse_pointer.pointer()
    shop_exit_but = button_class.button('back_arrow.png', 50, 650, 30, 30)

    font = load_font('Alice_in_Wonderland.ttf', 30)

    att_but = button_class.button('shop_att.png', 250, 350, 150, 150)
    potion_but = button_class.button('shop_potion.png', 750, 350, 150, 150)
    pass

def exit():
    global background
    global main_pointer
    global shop_exit_but
    global font
    global att_but
    global potion_but
    global money

    del money
    del(background)
    del(main_pointer)
    del(shop_exit_but)
    del(font)
    del(att_but)
    del(potion_but)
    pass

def handle_events():
    global main_pointer
    global shop_exit_but
    global att_but
    global potion_but

    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type in (SDL_MOUSEBUTTONUP, SDL_MOUSEBUTTONDOWN, SDL_MOUSEMOTION):
            main_pointer.update(event.x, 700 - event.y)
            shop_exit_but.mousemove_on(event.x, 700 - event.y)
            att_but.mousemove_on(event.x, 700 - event.y)
            potion_but.mousemove_on(event.x, 700 - event.y)

            if event.button == SDL_BUTTON_LEFT and event.type == SDL_MOUSEBUTTONUP:
                if att_but.get_mouse_on() \
                        and global_parameters.my_money >= global_parameters.shop_att_level * 200:
                    global_parameters.my_money -= global_parameters.shop_att_level * 200
                    global_parameters.shop_att_level+=1
                    global_parameters.global_snd.play_snd('button')

                if potion_but.get_mouse_on() \
                        and global_parameters.my_money >= global_parameters.shop_potion_level * 200:
                    global_parameters.my_money -= global_parameters.shop_potion_level * 200
                    global_parameters.shop_potion_level += 1
                    global_parameters.global_snd.play_snd('button')

                if shop_exit_but.get_mouse_on():
                    global_parameters.global_snd.play_snd('button')
                    game_framework.change_state(level_state)

def draw():
    global background
    global main_pointer
    global shop_exit_but
    global font
    global att_but
    global potion_but
    global money

    clear_canvas()
    hide_cursor()
    background.draw(width/2, height/2)
    shop_exit_but.draw()

    money.draw(820, 550, 50, 50)
    font.draw(850, 550, '%d' % global_parameters.my_money, (50, 50, 50))
    font.draw(att_but.m_x, att_but.m_y - 180, '%d' % global_parameters.shop_att_level, (50, 50, 50))
    font.draw(potion_but.m_x, potion_but.m_y - 180, '%d' % global_parameters.shop_potion_level, (50, 50, 50))

    att_but.draw()
    potion_but.draw()

    main_pointer.draw(0)
    update_canvas()
    pass


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass

