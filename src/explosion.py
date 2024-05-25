
import pyxel as px

from sprite import Sprite
from audio import play_sound, SoundType

FRAMES = ((0,64), (16,64), (32,64))
MAX_FRAMES = len(FRAMES)
FRAME_DELAY = 5

class Explosion(Sprite):
    def __init__(self, game_state, x, y, delay) -> None:
        super().__init__(game_state)
        self.x = x
        self.y = y
        self.delay = delay
        self.frame = 0
        self.frame_delay = FRAME_DELAY
        self.u = FRAMES[self.frame][0]
        self.v = FRAMES[self.frame][1]

        if self.delay == 0:
            self.sound()

    def sound(self):
        play_sound(SoundType.EXPLODE_SMALL)

    def update(self):
        if self.delay > 0:
            self.delay -= 1
            if self.delay == 0:
                self.sound()
            return
        
        self.frame_delay -= 1
        if self.frame_delay == 0:
            self.frame += 1
            if self.frame == MAX_FRAMES:
                self.remove = True
                return
            self.frame_delay = FRAME_DELAY
            self.u = FRAMES[self.frame][0]
            self.v = FRAMES[self.frame][1]
        
    def draw(self):
        if self.delay > 0:
            return
        
        super().draw()
