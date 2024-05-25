
from enemy import Enemy

BULLET_SPEED = 2

class EnemyC(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 13 # purple
        self.u = 32
        self.v = 80

        self.flip_y = True if self.y < 96 else False

        self.speed = state.get_scroll_x_speed()

    def update(self):
        super().update() # hit frames

        self.speed = self.game_state.get_scroll_x_speed()

        self.x -= self.speed
        if self.x + self.w < 0:
            self.remove = True
            return

        if self.lifetime == 25 or self.lifetime == 50:
            self.shoot_at_player(BULLET_SPEED)
