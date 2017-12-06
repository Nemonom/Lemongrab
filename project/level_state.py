import global_parameters
import game_framework
import main_state
import game_state
import mouse_pointer
import button_class
import shop_state

from pico2d import *


name = "level_state"
image = None
level_exit_but = None
easy_but = None
hard_but = None
shop_but = None
width = global_parameters.width
height = global_parameters.height

def enter():
    global background
    global main_pointer
    global level_exit_but
    global easy_but
    global hard_but
    global shop_but

    background = load_image('level.png')
    main_pointer = mouse_pointer.pointer()
    level_exit_but = button_class.button('back_arrow.png', 50, 650, 30, 30)
    easy_but = button_class.button('easy_button.png', 250, 350, 200, 100)
    hard_but = button_class.button('hard_button.png', 750, 350, 200, 100)
    shop_but = button_class.button('shop_button.png', 850, 650, 50, 50)
    pass

def exit():
    global background
    global main_pointer
    global level_exit_but
    global easy_but
    global hard_but
    global shop_but

    del(background)
    del(main_pointer)
    del(level_exit_but)
    del(easy_but)
    del(hard_but)
    del(shop_but)
    pass

def handle_events():
    global main_pointer
    global level_exit_but
    global easy_but
    global hard_but

    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type in (SDL_MOUSEBUTTONUP, SDL_MOUSEBUTTONDOWN, SDL_MOUSEMOTION):
            main_pointer.update(event.x, 700 - event.y)
            easy_but.mousemove_on(event.x, 700 - event.y)
            hard_but.mousemove_on(event.x, 700 - event.y)
            shop_but.mousemove_on(event.x, 700 - event.y)
            level_exit_but.mousemove_on(event.x, 700 - event.y)

            if event.button == SDL_BUTTON_LEFT and event.type == SDL_MOUSEBUTTONUP:
                if easy_but.get_mouse_on():
                    global_parameters.game_level = 0
                    game_framework.change_state(game_state)
                    break
                if shop_but.get_mouse_on():
                    global_parameters.game_level = 0
                    game_framework.change_state(shop_state)
                    break
                if hard_but.get_mouse_on():
                    global_parameters.game_level = 1
                    game_framework.change_state(game_state)
                    break
                if level_exit_but.get_mouse_on():
                    game_framework.change_state(main_state)


def draw():
    global background
    global main_pointer
    global level_exit_but
    global easy_but
    global hard_but
    global shop_but

    clear_canvas()
    hide_cursor()
    background.draw(width/2, height/2)
    level_exit_but.draw()
    easy_but.draw()
    hard_but.draw()
    shop_but.draw()
    main_pointer.draw(0)
    update_canvas()
    pass





def update():
    pass


def pause():
    pass


def resume():
    pass

