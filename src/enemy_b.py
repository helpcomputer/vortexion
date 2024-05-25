
import pyxel as px

from enemy import Enemy
from const import PI

SPEED = 1.5

BULLET_SPEED = 2

class EnemyB(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 3 # light green
        self.u = 16
        self.v = 80

    def update(self):
        super().update() # hit frames

        self.x -= SPEED
        if self.x + self.w < 0:
            self.remove = True
            return
    
        self.y += px.sin(self.lifetime * PI)

        if self.lifetime == 20:
            self.shoot_at_player(BULLET_SPEED)

