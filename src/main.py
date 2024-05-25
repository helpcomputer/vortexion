
import pyxel as px
from game import Game

from const import APP_WIDTH, APP_HEIGHT, APP_NAME, APP_DISPLAY_SCALE, \
    APP_CAPTURE_SCALE, APP_FPS, APP_GFX_FILE, PALETTE, SOUNDS_RES_FILE
from monospace_bitmap_font import MonospaceBitmapFont
from input import Input

class App:
    def __init__(self) -> None:
        px.init(
            APP_WIDTH, APP_HEIGHT, 
            title=APP_NAME,
            fps=APP_FPS,
            display_scale=APP_DISPLAY_SCALE,
            capture_scale=APP_CAPTURE_SCALE
        )

        px.colors.from_list(PALETTE)
        px.images[0].load(0, 0, "assets/" + APP_GFX_FILE)
        px.load("assets/" + SOUNDS_RES_FILE, excl_images=True, 
                excl_tilemaps=True, excl_musics=True)

        self.main_font = MonospaceBitmapFont()
        self.input = Input()

        self.game = Game(self)

        px.run(self.update, self.draw)
    
    def update(self):
        self.input.update()
        self.game.update()
    
    def draw(self):
        px.cls(0)
        self.game.draw()
    
if __name__ == "__main__":
    App()
