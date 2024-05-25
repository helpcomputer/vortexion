
from const import APP_WIDTH, EntityType
from sprite import Sprite

MAX_SHOTS = 4
UV_FRAME_OFFSET = 1
SIZE = 14
UV_OFFSET_Y = 16

SPEED_LVL = ( 10, 10, 11, 11, 12, 12 )
DAMAGE = {
    0 : [1, 1, 1, 1, 1, 2], # fwd
    1 : [1, 1, 1, 2, 2, 3], # spread/diagonal
    2 : [1, 1, 2, 2, 3, 3], # back/fwd
}

class PlayerShot(Sprite):
    def __init__(self, state, x, y, type, lvl, velx, vely) -> None:
        super().__init__(state)
        self.type = EntityType.PLAYER_SHOT
        self.x = x
        self.y = y
        self.w = SIZE
        self.h = SIZE

        self.u = (lvl * 16) + UV_FRAME_OFFSET
        self.v = UV_OFFSET_Y + (type * 16) + UV_FRAME_OFFSET

        self.velx = velx
        self.vely = vely

        self.damage = DAMAGE[type][lvl]

    def collide_background(self, bg):
        if bg.is_point_colliding(self.x + 7, self.y + 7): # centre pixel
            self.collided_with(bg)
            return True
        return False

    def collided_with(self, other):
        self.remove = True

    def update(self):
        self.x += self.velx
        self.y += self.vely

        if self.collide_background(self.game_state.background):
            return

        if self.x > APP_WIDTH or self.x + self.w < 0 or \
            self.y < 16 or self.y + self.h >= 176:
            self.remove = True
    
    def draw(self):
        super().draw()

def create(gs, player_x, player_y, wpn_type, wlvl):
    if len(gs.player_shots) >= MAX_SHOTS:
        return False
    
    addshot = gs.add_player_shot
    if wpn_type == 0: # fwd
        addshot(PlayerShot(gs, player_x + 12, player_y - 10, 
                           wpn_type, wlvl, SPEED_LVL[wlvl], 0))
        addshot(PlayerShot(gs, player_x + 12, player_y + 4, 
                           wpn_type, wlvl, SPEED_LVL[wlvl], 0))
    elif wpn_type == 1: # spread/diagonal
        spdx = SPEED_LVL[wlvl] * 0.894
        spdy = SPEED_LVL[wlvl] * 0.447
        addshot(PlayerShot(gs, player_x + 12, player_y - 10, 
                           wpn_type, wlvl, spdx, -spdy))
        addshot(PlayerShot(gs, player_x + 12, player_y + 4, 
                           wpn_type, wlvl, spdx, +spdy))
    elif wpn_type == 2: # back and fwd
        addshot(PlayerShot(gs, player_x + 12, player_y - 3, 
                           wpn_type, wlvl, SPEED_LVL[wlvl], 0))
        addshot(PlayerShot(gs, player_x - 10, player_y - 3, 
                           wpn_type, wlvl, -SPEED_LVL[wlvl], 0))

    return True