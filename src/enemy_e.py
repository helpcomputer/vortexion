
from enemy import Enemy

SPEED = 1
BULLET_SPEED = 2

class EnemyE(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 10 # yellow
        self.u = 64
        self.v = 80
        # spawn on left
        self.x -= 256 + 16

    def update(self):
        super().update() # hit frames

        self.x += SPEED
        if self.x > 255:
            self.remove = True
            return
        
        if self.lifetime == 200:
            self.shoot_at_angle(BULLET_SPEED, 180)

