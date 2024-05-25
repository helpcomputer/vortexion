
import pyxel as px

class MonospaceBitmapFont:
    def __init__(self) -> None:
        self.width = 8
        self.height = 8
        self.uv_chars_wide = 32 # chars per image width
        self.u_offset = 0
        self.v_offset = 240
    
    def draw_text(self, x, y, text):
        for char in text:
            code = ord(char)
            if code < 32 or code > 95:
                x += self.width
                continue
            code -= 32
            px.blt(x, y, 0, 
                   self.u_offset + \
                    (px.floor(code % self.uv_chars_wide) * self.width), 
                   self.v_offset + \
                    (px.floor(code / self.uv_chars_wide) * self.height), 
                   self.width, self.height)
            x += self.width
        