
from enum import IntEnum, auto

import pyxel as px
from sprite import Sprite
from const import MAX_COLOURS, EntityType, MAX_WEAPONS, PI
from audio import play_sound, SoundType

SPEED = 1

class PowerupType(IntEnum):
    NONE = 0
    LIFE = auto()
    WEAPON = auto()
    BOMB = auto()

FRAME_UV = (
    (0,0),
    (16,0),
    (32,0),
    (80,0),
    )

WEAPON_FRAME_UV = (
    (32,0),
    (48,0),
    (64,0),
    )

TYPE_CYCLE = [
    PowerupType.WEAPON,
    PowerupType.WEAPON,
    PowerupType.BOMB,
    PowerupType.WEAPON,
    PowerupType.LIFE,
    PowerupType.WEAPON,
    PowerupType.BOMB,
    ]
MAX_CYCLE_LEN = len(TYPE_CYCLE)
MAX_CYCLE_GAP_LEN = 8 # every n enemies killed spawn next pup

class Powerup(Sprite):
    type_cycle_index = 0
    type_cycle_gap_cnt = 0

    @classmethod
    def reset_cycle(cls):
        cls.type_cycle_index = 0
        cls.type_cycle_gap_cnt = 0

    @classmethod
    def is_cycle_ready(cls):
        cls.type_cycle_gap_cnt += 1
        if cls.type_cycle_gap_cnt == MAX_CYCLE_GAP_LEN:
            cls.type_cycle_gap_cnt = 0
            cls.type_cycle_index += 1
            if cls.type_cycle_index == MAX_CYCLE_LEN:
                cls.type_cycle_index = 0
            return True
        return False


    def __init__(self, game_state, type, x, y) -> None:
        super().__init__(game_state)
        self.type = EntityType.POWERUP
        self.x = x
        self.y = y
        self.puptype = type
        self.weapon_type = 0

        self.colour = 2
        self.u = FRAME_UV[self.puptype][0]
        self.v = FRAME_UV[self.puptype][1]

    def collected(self):
        self.remove = True
        if self.puptype == PowerupType.LIFE:
            play_sound(SoundType.LIFE_POWERUP, priority=True)
            self.game_state.game.game_vars.add_life()
        elif self.puptype == PowerupType.WEAPON:
            play_sound(SoundType.WEAPON_POWERUP, priority=True)
            self.game_state.game.game_vars.change_weapon(self.weapon_type)
            self.game_state.game.game_vars.add_current_weapon_level()
        elif self.puptype == PowerupType.BOMB:
            play_sound(SoundType.BOMB_POWERUP, priority=True)
            self.game_state.trigger_bomb()

    def collided_with(self, other):
        if other.type == EntityType.PLAYER:
            self.collected()

    def update(self):
        self.x -= 0.5
        if self.x + self.w < 0:
            self.remove = True
            return
        
        self.y += px.sin(px.frame_count * PI)

        if px.frame_count % 5 == 0:
            self.colour += 1
            if self.colour == MAX_COLOURS:
                self.colour = 2

        if px.frame_count % 60 == 0:
            if self.puptype == PowerupType.WEAPON:
                self.weapon_type += 1
                if self.weapon_type == MAX_WEAPONS:
                    self.weapon_type = 0
                self.u = WEAPON_FRAME_UV[self.weapon_type][0]
                self.v = WEAPON_FRAME_UV[self.weapon_type][1]
    
    def draw(self):
        px.pal(15, self.colour)
        super().draw()
        px.pal()

def check_create_next(state, x, y):
    if Powerup.is_cycle_ready():
        state.add_powerup(
        Powerup(state, TYPE_CYCLE[Powerup.type_cycle_index], x, y))
    