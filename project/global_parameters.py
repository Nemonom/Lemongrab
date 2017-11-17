#timer
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

MON_SPEED_KMPH = 20.0
MON_RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
MON_RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
MON_RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

#window
width = 1000
height = 700

#mouse
mouse_pointer_size = 30

#level
game_level = 0

#shop
shop_def_level, shop_att_level, shop_item_level = 1, 1, 1
my_money = 0


#tile
tile_size_x, tile_size_y = 100, 100

#object
player_size_x, player_size_y = 80, 80
player_att, player_hp, player_mp = 5, 100, 100


mon_size_x, mon_size_y = 20, 80
mon_hp, mon_att, mon_spd = 20, 5, 5

item_size = 20

hp_item, mp_item = 5, 5

#UI
icon_size_x, icon_size_y = 100, 100

ect_size_x, ect_size_y= 35, 35