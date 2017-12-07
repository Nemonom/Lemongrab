import global_parameters
import game_framework
import main_state

from pico2d import *

hide_cursor()

name = "logo_state"
image = None
logo_time = 0.0
logo_rotate = 0.0
width = global_parameters.width
height = global_parameters.height

def enter():
    global logo
    global logo_back
    global width, height

    open_canvas(width, height)
    logo = load_image('logo.png')
    logo_back = load_image('logo_back.png')

def exit():
    global logo
    global logo_back

    del(logo)
    del(logo_back)
    close_canvas()

def update(frame_time):
    global logo_time

    if(logo_time > 2.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state((main_state))
    delay(0.01)
    logo_time += 0.01

def draw():
    global logo
    global logo_back
    global logo_rotate
    global width, height

    clear_canvas()
   # logo.draw(500, 350)
    logo_back.draw(width/2, height/2)
    logo.rotate_draw(logo_rotate, width/2, height/2, width - logo_rotate * 50, height - logo_rotate * 50)

    update_canvas()
    if(logo_time > 1.3):
        logo_rotate += 0.2
def handle_events():
    pass


def pause(): pass


def resume(): pass




