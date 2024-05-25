
import pyxel as px

from enemy_spawn import ENEMY_SPAWN_TILE_INDEX_Y
import enemy_spawn
from const import EntityType
from audio import reset_music_gain, fade_out_music, \
    SOUND_CHANNEL_GAIN_DEFAULT

VIEW_WIDTH = 256
VIEW_HEIGHT = 160
MAP_WIDTH = 2048
MAP_WIDTH_VORTEX = 1024
MAP_HEIGHT = 160
MAP_HEIGHT_TILES = MAP_HEIGHT // 8

TILES_TM_INDEX = 0
ENEMIES_TM_INDEX = 1

SOLID_TILE_START_ROW = 176//8

SCROLL_X_STOP_STAGE_MUSIC = 208 * 8
SCROLL_X_START_BOSS_MUSIC = 223 * 8

class StageBackground:
    def __init__(self, state_stage, map_file, is_vortex) -> None:
        self.type = EntityType.BACKGROUND
        self.state_stage = state_stage
        self.scroll_x = 0
        self.scroll_x_speed = 0.5

        if is_vortex:
            self.map_width = MAP_WIDTH_VORTEX
        else:
            self.map_width = MAP_WIDTH

        self.is_vortex = is_vortex
        self.vortex_scroll_x = 0
        self.vortex_scroll_x_speed = 8

        px.tilemaps[TILES_TM_INDEX] = \
            px.Tilemap.from_tmx("assets/" + map_file, TILES_TM_INDEX)
        px.tilemaps[ENEMIES_TM_INDEX] = \
            px.Tilemap.from_tmx("assets/" + map_file, ENEMIES_TM_INDEX)
        
        self.last_col_checked = 0

        self.music_gain = SOUND_CHANNEL_GAIN_DEFAULT

    def get_tile(self, tile_x, tile_y):
        return px.tilemaps[TILES_TM_INDEX].pget(tile_x, tile_y)

    def is_point_colliding(self, x, y):
        y -= 16 # offset screen pixels due to hud
        return self.get_tile(x//8, y//8)[1] >=  SOLID_TILE_START_ROW

    def check_next_enemy_spawn(self):
        col = (self.scroll_x + VIEW_WIDTH) // 8
        if col > self.last_col_checked:
            self.last_col_checked = col
            for row in range(MAP_HEIGHT_TILES):
                tile = px.tilemaps[ENEMIES_TM_INDEX].pget(col, row)
                if tile[1] == ENEMY_SPAWN_TILE_INDEX_Y:
                    enemy_spawn.create(self.state_stage, 
                                       tile[0] << 3, 
                                       col*8 - self.scroll_x, 
                                       16 + row*8)
                    row += 1 # skip down as one below wont be another enemy

    def update(self):
        if self.scroll_x < self.map_width - VIEW_WIDTH:
            self.scroll_x += self.scroll_x_speed
        else:
            self.scroll_x_speed = 0
            # No boss on vortex stage, end immediately once at end.
            if self.is_vortex:
                self.state_stage.end_of_vortex_stage()

        if self.scroll_x >= SCROLL_X_STOP_STAGE_MUSIC and \
            self.scroll_x < SCROLL_X_START_BOSS_MUSIC:
            self.music_gain = fade_out_music(self.music_gain, 3)
        elif self.scroll_x == SCROLL_X_START_BOSS_MUSIC:
            reset_music_gain(3)
            self.state_stage.play_boss_music()

        self.check_next_enemy_spawn()

        if self.is_vortex:
            self.vortex_scroll_x -= self.vortex_scroll_x_speed
            if self.vortex_scroll_x <= -VIEW_WIDTH:
                self.vortex_scroll_x += VIEW_WIDTH
    
    def draw(self):
        if self.is_vortex:
            px.bltm(self.vortex_scroll_x, 16, TILES_TM_INDEX, 
                    0, 0, VIEW_WIDTH, VIEW_HEIGHT)
            px.bltm(self.vortex_scroll_x + VIEW_WIDTH, 16, TILES_TM_INDEX, 
                    0, 0, VIEW_WIDTH, VIEW_HEIGHT)
        else:
            px.bltm(0, 16, TILES_TM_INDEX, 
                    self.scroll_x, 0, 
                    VIEW_WIDTH, VIEW_HEIGHT)
    