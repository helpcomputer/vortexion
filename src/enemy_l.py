
import pyxel as px

from enemy import Enemy
from const import ENEMY_SCORE_BOSS

BULLET_SPEED = 1.5

# Boss: large leaves
class EnemyL(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 3 # light green
        self.u = 176
        self.v = 80

        self.w = 32
        self.h = 32
        self.hp = 100
        self.score = ENEMY_SCORE_BOSS

        self.speed_x = state.get_scroll_x_speed()

    def shoot(self):
        self.shoot_at_player(BULLET_SPEED)
        self.shoot_at_player(BULLET_SPEED, 5)

    def update(self):
        super().update() # hit frames

        self.speed_x = self.game_state.get_scroll_x_speed()

        self.x -= self.speed_x
        
        if self.game_state.get_num_enemies() == 0:
            if self.lifetime % 60 == 0:
                self.shoot()
        else:
            if self.lifetime % 200 == 0:
                self.shoot()

    def explode(self):
        for i in range(6):
            self.game_state.add_explosion(
                self.x + 8 + px.rndi(-12,12), 
                self.y + 8 + px.rndi(-6,6), i*5)

    def destroy(self):
        super().destroy()
        self.game_state.check_stage_clear = True

    def draw_composite(self, is_hit):
        # top left
        px.blt(self.x, self.y, 0,
               self.u, self.v, 16, 16, 0)
        # top right
        if not is_hit:
            px.pal(self.colour, 2) # green
        px.blt(self.x + 16, self.y, 0,
               self.u, self.v, -16, 16, 0)
        # bottom left
        if not is_hit:
            px.pal(self.colour, 12) # dark green
        px.blt(self.x, self.y + 16, 0,
               self.u, self.v, 16, -16, 0)
        # bottom right
        if not is_hit:
            px.pal(self.colour, 5) # lght blue
        px.blt(self.x + 16, self.y + 16, 0,
               self.u, self.v, -16, -16, 0)
        
        if not is_hit:
            px.pal()

    def draw(self):
        if self.hit_frames > 0:
            px.pal(self.colour, 15)
            self.draw_composite(True)
            px.pal()
        else:
            self.draw_composite(False)

