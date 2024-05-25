
from enemy import Enemy

SPEED_X = 4
SPEED_Y = 0.5

class EnemyN(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 14 # grey
        self.u = 208
        self.v = 80

        self.hp = 1

        if self.y < 96:
            self.speed_y = SPEED_Y
        else:
            self.speed_y = -SPEED_Y

    def update(self):
        super().update() # hit frames

        self.x -= SPEED_X
        if self.x + self.w < 0:
            self.remove = True
            return
        
        self.y += self.speed_y
    