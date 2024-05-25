
import pyxel as px

import input
from hud import Hud
from const import APP_VERSION
from audio import load_music, play_music

VIEW_WIDTH = 256
MAP_HEIGHT = 160
BG_SCROLL_SPD = 8
TILEMAP_FILE = "title.tmx"
MUSIC_FILE = "music_title.json"
BG_TM_INDEX = 0
FG_TM_INDEX = 1

class GameStateTitles:
    def __init__(self, game) -> None:
        self.game = game
        self.input = self.game.app.input
        self.font = game.app.main_font

        self.hud = Hud(game.game_vars, self.font)

        px.tilemaps[BG_TM_INDEX] = \
            px.Tilemap.from_tmx("assets/" + TILEMAP_FILE, 
                                BG_TM_INDEX)
        px.tilemaps[FG_TM_INDEX] = \
            px.Tilemap.from_tmx("assets/" + TILEMAP_FILE, 
                                FG_TM_INDEX)
        
        self.scroll_x = 0
        
        self.selections = {
            0 : {
                "loc" : [96,112],
                "label" : "GAME START",
                "action" : self.game.go_to_new_game,
                },
            1 : {
                "loc" : [96,128],
                "label" : "CONTINUE",
                "action" : self.game.go_to_continue,
                },
        }
        
        self.selected_index = 0

        self.music = load_music(MUSIC_FILE)
        play_music(self.music)
    
    def on_exit(self):
        px.stop()

    def update(self):
        self.scroll_x -= BG_SCROLL_SPD
        if self.scroll_x <= -VIEW_WIDTH:
            self.scroll_x += VIEW_WIDTH

        if self.input.has_tapped(input.UP) or \
            self.input.has_tapped(input.DOWN):
            self.selected_index = 0 if self.selected_index == 1 else 1

        if self.input.has_tapped(input.BUTTON_1) or \
            self.input.has_tapped(input.BUTTON_2):
            (self.selections[self.selected_index]["action"])()
    
    def draw(self):
        px.bltm(self.scroll_x, 16, BG_TM_INDEX, 
                0, 0, VIEW_WIDTH, MAP_HEIGHT)
        px.bltm(self.scroll_x + VIEW_WIDTH, 16, BG_TM_INDEX, 
                0, 0, VIEW_WIDTH, MAP_HEIGHT)
        
        px.bltm(0, 16, FG_TM_INDEX, 0, 0, VIEW_WIDTH, MAP_HEIGHT, 0)

        for k, v in self.selections.items():
            loc = v["loc"]
            if k == self.selected_index:
                px.blt(loc[0] - 16, loc[1] - 4, 0, 0, 0, 16, 16, 0)
            self.font.draw_text(loc[0], loc[1], v["label"])

        self.hud.draw()

        px.text(8, 152, f"v{APP_VERSION}", 4)
    