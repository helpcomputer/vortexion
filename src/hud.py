
import pyxel as px

from const import MAX_WEAPONS, MAX_WEAPON_LEVEL, WEAPON_NAMES

class Hud:
    def __init__(self, game_vars, font) -> None:
        self.game_vars = game_vars
        self.font = font
    
    def draw_weapon_level(self, i, x, y):
        self.font.draw_text(x + 16, y, WEAPON_NAMES[i])
        px.blt(x + 24, y, 0, i * 16, 224, 16, 8)

        j = 0
        while j <= self.game_vars.weapon_levels[i]:
            px.blt(x + (j * 8), y + 8, 0, 32, 232, 8, 8)
            j += 1
        while j <= MAX_WEAPON_LEVEL:
            px.blt(x + (j * 8), y + 8, 0, 40, 232, 8, 8)
            j += 1

    def draw(self):
        # top and bottom bg
        px.rect(0,0, 256, 16, 1)
        px.rect(0,176, 256, 16, 1)

        # top
        self.font.draw_text(24, 0, "1UP")
        self.font.draw_text(16, 8, f"{self.game_vars.score:06}")

        self.font.draw_text(96, 0, "HI-SCORE")
        self.font.draw_text(104, 8, f"{self.game_vars.hi_score:06}")

        self.font.draw_text(176, 0, "ARM")
        self.font.draw_text(176, 8, WEAPON_NAMES[self.game_vars.current_weapon])
        px.blt(184, 8, 0, self.game_vars.current_weapon * 16, 224, 16, 8)

        px.blt(216, 0, 0, 0, 4, 16, 8, 0)
        self.font.draw_text(224, 8, f"{self.game_vars.lives}")

        # bottom
        self.font.draw_text(16, 176, "ARM")
        self.font.draw_text(16, 184, "LVL")

        for i in range(MAX_WEAPONS):
            self.draw_weapon_level(i, 56 + (64 * i), 176)
