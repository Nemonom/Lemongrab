import game_framework
import main_state

from pico2d import *


name = "logo_state"
image = None
logo_time = 0.0


def enter():
    global logo
    open_canvas(1000, 700)
    logo = load_image('logo.png')

def exit():
    global image
    del(image)
    close_canvas()

def update():
    global logo_time

    if(logo_time > 2.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state((main_state))
    delay(0.01)
    logo_time += 0.01
    
def draw():
    global logo
    clear_canvas()
    logo.draw(500, 350)
    update_canvas()

def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




