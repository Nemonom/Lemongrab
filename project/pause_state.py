import global_parameters
import game_framework
import game_state


from pico2d import *


name = "pause_state"
pause_img = None
pause_back = None

width = global_parameters.width
height = global_parameters.height

logo_time = None

def enter():
    global pause_img
    global logo_time
    global pause_back

    logo_time = 0
    pause_img = load_image('pause.png')
    pause_back = load_image('pause_back.png')
    pass

def exit():
    global pause_img
    global pause_back

    del (pause_back)
    del (pause_img)
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.key == SDLK_SPACE:
            game_framework.pop_state()


def draw():
    global pause_img
    global logo_time
    global pause_back

    clear_canvas()
    game_state.game_draw()
    pause_back.draw(width/2, height/2)
    if logo_time < 2:
        pause_img.draw(width / 2, height / 2)
    update_canvas()
    pass


def update(frame_time):
    global logo_time
    logo_time = logo_time + frame_time
    if logo_time > 3:
        logo_time = 0
    pass


def pause():
    pass


def resume():
    pass

