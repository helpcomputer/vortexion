
from enemy import Enemy

BULLET_SPEED = 2

class EnemyF(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 2 # green
        self.u = 80
        self.v = 80

        self.flip_y = True if self.y < 96 else False
        self.speed_x = state.get_scroll_x_speed()

    def shoot(self):
        # top
        if self.y < 96:
            self.shoot_at_angle(BULLET_SPEED, 90)
            self.shoot_at_angle(BULLET_SPEED, 110)
            self.shoot_at_angle(BULLET_SPEED, 130)
        else: # bottom
            self.shoot_at_angle(BULLET_SPEED, 230)
            self.shoot_at_angle(BULLET_SPEED, 250)
            self.shoot_at_angle(BULLET_SPEED, 270)
            
    def update(self):
        super().update() # hit frames

        self.speed_x = self.game_state.get_scroll_x_speed()

        self.x -= self.speed_x
        if self.x + self.w < 0:
            self.remove = True
            return
        
        if self.lifetime == 100 or self.lifetime == 200 or \
            self.lifetime == 300:
            self.shoot()

