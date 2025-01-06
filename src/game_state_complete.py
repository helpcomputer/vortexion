
import pyxel as px

import input
from hud import Hud
from const import MUSIC_GAME_COMPLETE
from audio import load_music, play_music, stop_music

VIEW_WIDTH = 256
MAP_HEIGHT = 192
BG_SCROLL_SPD = 8
TITLE_SCREEN_MAP_FILE = "complete.tmx"
BG_TM_INDEX = 0

class GameStateComplete:
    def __init__(self, game) -> None:
        self.game = game
        self.input = self.game.app.input
        self.font = game.app.main_font

        self.hud = Hud(game.game_vars, self.font)

        px.tilemaps[BG_TM_INDEX] = \
            px.Tilemap.from_tmx("assets/" + TITLE_SCREEN_MAP_FILE, 
                                BG_TM_INDEX)
        
        self.scroll_x = 0

        self.music = load_music(MUSIC_GAME_COMPLETE)
        play_music(self.music, True, num_channels=3)
    
    def on_exit(self):
        stop_music(3)

    def update(self):
        self.scroll_x -= BG_SCROLL_SPD
        if self.scroll_x <= -VIEW_WIDTH:
            self.scroll_x += VIEW_WIDTH

        if self.input.has_tapped(input.BUTTON_1) or \
            self.input.has_tapped(input.BUTTON_2):
            self.game.go_to_titles()
    
    def draw(self):
        px.bltm(self.scroll_x, 0, BG_TM_INDEX, 
                0, 0, VIEW_WIDTH, MAP_HEIGHT)
        px.bltm(self.scroll_x + VIEW_WIDTH, 0, BG_TM_INDEX, 
                0, 0, VIEW_WIDTH, MAP_HEIGHT)

        self.font.draw_text(56, 72, "THANKS FOR PLAYING")
        self.font.draw_text(88, 96, "FINAL SCORE")
        self.font.draw_text(104, 112, f"{self.game.game_vars.score}")
    