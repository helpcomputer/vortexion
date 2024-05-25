
from enemy import Enemy

SPEED_Y = 2

class EnemyD(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 14 # grey
        self.u = 48
        self.v = 80

        self.flip_y = True if self.y < 96 else False

        self.vx = state.get_scroll_x_speed() + 0.25
        self.vy = 0

    def update(self):
        super().update() # hit frames

        self.x -= self.vx
        if self.x + self.w < 0:
            self.remove = True
            return
        
        if self.vy == 0:
            if self.x - self.game_state.player.x < 24:
                self.vy = SPEED_Y if self.y < 96 else -SPEED_Y
        else:
            self.y += self.vy
            if self.y + self.h < 16 or self.y > 176:
                self.remove = True
