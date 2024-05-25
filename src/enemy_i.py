
from enemy import Enemy

BULLET_SPEED = 1.5
SPEED = 1.5
VEL_Y = [-0.5, 1, -1.25, 1.25, -1, 0.5]

class EnemyI(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 8 # red
        self.u = 128
        self.v = 80

        self.hp = 3

        self.vel_y_index = 0

    def update(self):
        super().update() # hit frames

        if self.vel_y_index < len(VEL_Y) - 1:
            if self.lifetime % 45 == 0:
                self.vel_y_index += 1

        self.y += VEL_Y[self.vel_y_index]

        if self.lifetime == 30:
            self.shoot_at_player(BULLET_SPEED)

        self.x -= SPEED
        if self.x + self.w < 0:
            self.remove = True
            return

