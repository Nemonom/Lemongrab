from pico2d import *

#player class
class my_bgm:
    title_bgm = None
    game_bgm = None
    title_on = False

    def __init__(self):
        pass

    def play_bgm(self, char):
        if char == 'title':
            if my_bgm.title_on == False:
               my_bgm.title_bgm = load_music('title bgm.mp3')
               my_bgm.title_bgm.set_volume(20)
               my_bgm.title_bgm.repeat_play()
               my_bgm.title_on = True
        if char == 'game':
            my_bgm.game_bgm = load_music('game bgm.mp3')
            my_bgm.game_bgm.set_volume(10)
            my_bgm.game_bgm.repeat_play()
        pass

    def stop_bgm(self, char):
        if char == 'title':
            my_bgm.title_bgm.stop()
            my_bgm.title_on = False
        if char == 'game':
            my_bgm.game_bgm.stop()



class my_snd:
    bullet_snd = None
    button_snd = None
    eat_snd = None

    def __init__(self):
       pass

    def play_snd(self, char):
        if char == 'bullet':
            my_snd.bullet_snd = load_wav('bullet-sound.wav')
            my_snd.bullet_snd.set_volume(20)
            self.bullet_snd.play()
        if char == 'button':
            my_snd.button_snd = load_wav('button-click.wav')
            my_snd.button_snd.set_volume(20)
            self.button_snd.play()
        if char == 'eat':
            my_snd.eat_snd = load_wav('stage-up.wav')
            my_snd.eat_snd.set_volume(20)
            self.eat_snd.play()
        pass
