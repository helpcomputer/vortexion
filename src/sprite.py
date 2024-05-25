
from itertools import filterfalse

import pyxel as px

from utils import rect_overlap

class Sprite:
    def __init__(self, game_state) -> None:
        self.game_state = game_state
        self.x = 0
        self.y = 0
        self.w = 16
        self.h = 16
        self.remove = False

        self.colour = 15 # white
        self.u = 0
        self.v = 0

        self.flip_x = False
        self.flip_y = False
        
    # def collided_with(self, other):
    #     pass

    # def update(self):
    #     pass
    
    def draw(self):
        w = -self.w if self.flip_x else self.w
        h = -self.h if self.flip_y else self.h
        px.blt(self.x, self.y, 0,
               self.u, self.v, w, h, 0)
    

def sprites_collide(a, b):
    return rect_overlap(a.x, a.y, a.w, a.h, b.x, b.y, b.w, b.h)

def sprites_update(the_list):
    for s in the_list:
        s.update()
    the_list[:] = filterfalse(lambda s: s.remove, the_list)

def sprites_draw(the_list):
    for s in the_list:
        s.draw()

def sprite_lists_collide(list_a, list_b):
    for a in list_a:
        if a.remove:
            continue
        for b in list_b:
            if b.remove:
                continue
            if sprites_collide(a, b):
                a.collided_with(b)
                b.collided_with(a)

def sprite_collide_list(spr, the_list):
    if spr.remove:
        return
    for a in the_list:
        if a.remove:
            continue
        if sprites_collide(spr, a):
            spr.collided_with(a)
            a.collided_with(spr)
