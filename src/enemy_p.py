
from enemy import Enemy

SPEED = 2.5
BULLET_SPEED = 4

SHOT_DELAY = 120

class EnemyP(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 9 # pink
        self.u = 240
        self.v = 80

        self.shot_delay = 25 # allow time to get on screen

    def update(self):
        super().update() # hit frames

        self.x -= SPEED
        if self.x + self.w < 0:
            self.remove = True
            return

        if self.shot_delay == 0:
            self.shot_delay = SHOT_DELAY
            self.shoot_at_angle(BULLET_SPEED, 190)
            self.shoot_at_angle(BULLET_SPEED, 170)
        else:
            self.shot_delay -= 1
    