
import pyxel as px

from const import APP_WIDTH, EntityType
from sprite import Sprite

SIZE = 4

class EnemyShot(Sprite):
    def __init__(self, game_state, x, y, vx, vy, delay=0) -> None:
        super().__init__(game_state)
        self.type = EntityType.ENEMY_SHOT
        self.x = x
        self.y = y
        self.w = SIZE
        self.h = SIZE
        self.vx = vx
        self.vy = vy

        self.colour = 11 # yellow
        self.u = 6
        self.v = 102

        self.delay = delay

    def collide_background(self, bg):
        if bg.is_point_colliding(self.x + 2, self.y + 2): # centre pixel
            self.collided_with(bg)
            return True
        return False

    def collided_with(self, other):
        if self.delay > 0:
            return
        if other.type == EntityType.PLAYER:
            if not other.is_invincible():
                self.remove = True

    def update(self):
        if self.delay > 0:
            self.delay -= 1
            return

        self.x += self.vx
        self.y += self.vy

        if self.collide_background(self.game_state.background):
            return

        if self.x > APP_WIDTH or self.x + self.w < 0 or \
            self.y < 16 or self.y + self.h >= 176:
            self.remove = True
            return

        if px.frame_count % 10 == 0:
            self.colour = 11 if (self.colour == 6) else 6

    def draw(self):
        if self.delay > 0:
            return

        px.pal(15, self.colour)
        super().draw()
        px.pal()