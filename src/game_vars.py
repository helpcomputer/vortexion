
from const import STARTING_LIVES, MAX_WEAPONS, MAX_SCORE, MAX_WEAPON_LEVEL,\
    MAX_LIVES, StageNum, FINAL_STAGE

class GameVars:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.hi_score = 0
        self.current_weapon = 0
        self.lives = STARTING_LIVES
        self.weapon_levels = []
        for _ in range(MAX_WEAPONS):
            self.weapon_levels.append(0)
        self.stage_num = StageNum.STAGE_1

    def is_vortex_stage(self):
        return self.stage_num % 2 == 0

    def new_game(self):
        self.continue_game()
        self.stage_num = StageNum.STAGE_1

    def continue_game(self):
        self.score = 0
        self.current_weapon = 0
        for i in range(len(self.weapon_levels)):
            self.weapon_levels[i] = 0
        self.lives = STARTING_LIVES

    def go_to_next_stage(self):
        if self.stage_num < FINAL_STAGE:
            self.stage_num = StageNum(self.stage_num + 1)
            return True
        return False

    def add_life(self):
        self.lives = min(MAX_LIVES, self.lives + 1)

    def subtract_life(self):
        self.lives = max(0, self.lives - 1)

    def add_score(self, s):
        self.score = min(MAX_SCORE, self.score + s)
        self.hi_score = max(self.score, self.hi_score)

    def decrease_all_weapon_levels(self, amount):
        for i in range(len(self.weapon_levels)):
            self.weapon_levels[i] = max(0, self.weapon_levels[i] - amount)

    def increase_all_weapon_levels(self, amount):
        for i in range(len(self.weapon_levels)):
            self.weapon_levels[i] = \
                min(MAX_WEAPON_LEVEL, self.weapon_levels[i] + amount)

    def change_weapon(self, new_wpn):
        self.current_weapon = new_wpn

    def add_current_weapon_level(self):
        self.weapon_levels[self.current_weapon] = \
            min(MAX_WEAPON_LEVEL, self.weapon_levels[self.current_weapon] + 1)

