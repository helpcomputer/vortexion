
import pyxel as px

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
BUTTON_1 = 4
BUTTON_2 = 5

class Input:
    def __init__(self):
        self.pressing = []
        self.tapped = []

    def is_pressing(self, i):
        return i in self.pressing
    
    def has_tapped(self, i):
        return i in self.tapped
        
    def update(self):
        self.pressing.clear()
        self.tapped.clear()
    
        # pressing
        if px.btn(px.KEY_UP) or px.btn(px.KEY_W) or \
            px.btn(px.GAMEPAD1_BUTTON_DPAD_UP):
            self.pressing.append(UP)
        elif px.btn(px.KEY_DOWN) or px.btn(px.KEY_S) or \
            px.btn(px.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.pressing.append(DOWN)
            
        if px.btn(px.KEY_LEFT) or px.btn(px.KEY_A) or \
            px.btn(px.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.pressing.append(LEFT)
        elif px.btn(px.KEY_RIGHT) or px.btn(px.KEY_D) or \
            px.btn(px.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.pressing.append(RIGHT)
        
        if px.btn(px.KEY_Z) or px.btn(px.KEY_U) or \
            px.btn(px.GAMEPAD1_BUTTON_A):
            self.pressing.append(BUTTON_1)
        
        if px.btn(px.KEY_X) or px.btn(px.KEY_I) or \
            px.btn(px.GAMEPAD1_BUTTON_B):
            self.pressing.append(BUTTON_2)
            
        # tapped
        if px.btnp(px.KEY_UP) or px.btnp(px.KEY_W) or \
            px.btnp(px.GAMEPAD1_BUTTON_DPAD_UP):
            self.tapped.append(UP)
        elif px.btnp(px.KEY_DOWN) or px.btnp(px.KEY_S) or \
            px.btnp(px.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.tapped.append(DOWN)
            
        if px.btnp(px.KEY_LEFT) or px.btnp(px.KEY_A) or \
            px.btnp(px.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.tapped.append(LEFT)
        elif px.btnp(px.KEY_RIGHT) or px.btnp(px.KEY_D) or \
            px.btnp(px.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.tapped.append(RIGHT)
        
        if px.btnp(px.KEY_Z) or px.btnp(px.KEY_U) or \
            px.btnp(px.GAMEPAD1_BUTTON_A):
            self.tapped.append(BUTTON_1)
        
        if px.btnp(px.KEY_X) or px.btnp(px.KEY_I) or \
            px.btnp(px.GAMEPAD1_BUTTON_B):
            self.tapped.append(BUTTON_2)
            