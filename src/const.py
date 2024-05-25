
from enum import Enum, IntEnum, auto

APP_VERSION = "1.0"
APP_WIDTH = 256
APP_HEIGHT = 192
APP_NAME = "VORTEXION"
APP_FPS = 60
APP_DISPLAY_SCALE = 2
APP_CAPTURE_SCALE = 2
APP_GFX_FILE = "gfx.png"

class StageNum(IntEnum):
    STAGE_1 = auto() # = 1
    STAGE_2 = auto() # vortex
    STAGE_3 = auto()
    STAGE_4 = auto() # vortex
    STAGE_5 = auto()
FINAL_STAGE = StageNum.STAGE_5

STAGE_MUSIC_FILES = {
    StageNum.STAGE_1 : "music_stage_1.json",
    StageNum.STAGE_2 : "music_vortex.json",
    StageNum.STAGE_3 : "music_stage_3.json",
    StageNum.STAGE_4 : "music_vortex.json",
    StageNum.STAGE_5 : "music_stage_5.json",
}
MUSIC_GAME_COMPLETE = "music_game_complete.json"
MUSIC_GAME_OVER = "music_game_over.json"
MUSIC_BOSS = "music_boss.json"
MUSIC_STAGE_CLEAR = "music_stage_clear.json"

class EntityType(Enum):
    PLAYER = 0
    PLAYER_SHOT = auto()
    ENEMY = auto()
    ENEMY_SHOT = auto()
    POWERUP = auto()
    BACKGROUND = auto()

STARTING_LIVES = 3
MAX_LIVES = 9
MAX_WEAPONS = 3
MAX_WEAPON_LEVEL = 5
WEAPON_NAMES = ["A", "B", "C"]
MAX_SCORE = 999999

ENEMY_SCORE_NORMAL = 100
ENEMY_SCORE_BOSS = 5000

PLAYER_SHOT_DAMAGE = 1
BOMB_DAMAGE = 30

PI = 3.141

MAX_COLOURS = 16
PALETTE = [
    0xFF00FF, # transparent
    0x000000,
    0x21c842,
    0x5edc78,

    0x5455ed,
    0x7d76fc,
    0xd4524d,
    0x42ebf5,

    0xfc5554,
    0xff7978,
    0xd4c154,
    0xe6ce80,

    0x21b03b,
    0xc95bba,
    0xcccccc,
    0xffffff
]

SOUNDS_RES_FILE = "sounds.pyxres"
