
from enemy import Enemy

BULLET_SPEED = 1.5

class EnemyJ(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 13 # purple
        self.u = 144
        self.v = 80

        self.hp = 40

        self.speed_x = state.get_scroll_x_speed()

    def update(self):
        super().update() # hit frames

        self.speed_x = self.game_state.get_scroll_x_speed()

        self.x -= self.speed_x
        if self.x + self.w < 0:
            self.remove = True
            return
        
        if self.lifetime % 120 == 0:
            self.shoot_at_angle(BULLET_SPEED, 210)
            self.shoot_at_angle(BULLET_SPEED, 195, 10)
            self.shoot_at_angle(BULLET_SPEED, 180, 20)
            self.shoot_at_angle(BULLET_SPEED, 165, 30)
            self.shoot_at_angle(BULLET_SPEED, 150, 40)

