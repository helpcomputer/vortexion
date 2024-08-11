
from enum import Enum, auto

import pyxel as px

from const import FINAL_STAGE, STAGE_MUSIC_FILES, MUSIC_GAME_OVER, MUSIC_BOSS,\
    MUSIC_STAGE_CLEAR
from player import Player
from sprite import sprites_update, sprites_draw, sprite_lists_collide, \
    sprite_collide_list
from hud import Hud
from explosion import Explosion
from powerup import Powerup
from stage_background import StageBackground
import input
from audio import load_music, play_music, is_music_playing, stop_music

class State(Enum):
    PLAYER_SPAWNED = 0
    PLAY = auto()
    PLAYER_DEAD = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    STAGE_CLEAR = auto()

PLAYER_SPAWN_IN_FRAMES = 30
STAGE_CLEAR_FRAMES = 180

class GameStateStage:
    def __init__(self, game) -> None:
        self.game = game
        self.state = State.PLAYER_SPAWNED
        self.input = game.app.input
        self.font = game.app.main_font

        self.state_time = 0

        self.player = Player(self)
        self.player_shots = []

        self.enemies = []
        self.enemy_shots = []
        self.bosses = []

        self.explosions = []

        self.powerups = []
        Powerup.reset_cycle()

        self.background = StageBackground(
            self, 
            f"stage_{game.game_vars.stage_num}.tmx",
            self.game.game_vars.is_vortex_stage())

        self.hud = Hud(game.game_vars, self.font)

        self.check_stage_clear = False

        self.music = load_music(
            STAGE_MUSIC_FILES[self.game.game_vars.stage_num])
        play_music(self.music, num_channels=3)

    def on_exit(self):
        px.stop()

    def end_of_vortex_stage(self):
        if self.state == State.PLAY:
            self.check_stage_clear = True

    def stage_clear_init(self):
        self.enemy_shots.clear()
        for e in self.enemies:
            e.destroy()
        self.switch_state(State.STAGE_CLEAR)
        if self.game.game_vars.stage_num < FINAL_STAGE:
            self.music = load_music(MUSIC_STAGE_CLEAR)
            play_music(self.music, False, 3, 620)
        else:
            stop_music()

    def respawn_player(self):
        self.player = Player(self)

    def get_scroll_x_speed(self):
        return self.background.scroll_x_speed

    def add_enemy(self, e):
        self.enemies.append(e)
        #print(f"Added enemy type {e.type} at {e.x//8},{e.y//8}")

    def add_boss(self, b):
        self.bosses.append(b)

    def add_powerup(self, p):
        self.powerups.append(p)

    def add_explosion(self, x, y, delay):
        self.explosions.append(Explosion(self, x, y, delay))

    def trigger_bomb(self):
        self.enemy_shots.clear()
        for e in self.enemies:
            e.hit_with_bomb()
        for b in self.bosses:
            b.hit_with_bomb()

    def add_score(self, amount):
        self.game.game_vars.add_score(amount)

    # Doesnt include bosses.
    def get_num_enemies(self):
        return len(self.enemies)
    
    def add_player_shot(self, s):
        self.player_shots.append(s)

    def add_enemy_shot(self, s):
        self.enemy_shots.append(s)

    def update_play(self):
        self.player.update()

    def switch_state(self, new):
        self.state = new
        self.state_time = 0
        #print(f"Switched stage state to {self.state}")

    def update_player_dead(self):
        if len(self.explosions) == 0:
            if self.game.game_vars.lives > 0:
                self.respawn_player()
                self.switch_state(State.PLAYER_SPAWNED)
            else:
                self.switch_state(State.GAME_OVER)
                self.music = load_music(MUSIC_GAME_OVER)
                play_music(self.music, False, num_channels=3)

    def play_boss_music(self):
        self.music = load_music(MUSIC_BOSS)
        play_music(self.music, True, num_channels=3)

    def update_game_over(self):
        if self.input.has_tapped(input.BUTTON_1) or \
            self.input.has_tapped(input.BUTTON_2) or \
            not is_music_playing():
            self.game.go_to_titles()

    def update_player_spawned(self):
        self.player.update_spawned()
        if self.state_time == PLAYER_SPAWN_IN_FRAMES:
            self.switch_state(State.PLAY)

    def update_stage_clear(self):
        if self.state_time >= STAGE_CLEAR_FRAMES and \
            not is_music_playing():
            self.game.go_to_next_stage()

    def update(self):
        self.state_time += 1

        if self.state == State.PLAYER_SPAWNED:
            self.update_player_spawned()
        elif self.state == State.PLAY:
            if self.input.has_tapped(input.BUTTON_2):
                self.switch_state(State.PAUSED)
                return
            self.update_play()
        elif self.state == State.PLAYER_DEAD:
            self.update_player_dead()
        elif self.state == State.PAUSED:
            if self.input.has_tapped(input.BUTTON_2):
                self.switch_state(State.PLAY)
            else:
                return
        elif self.state == State.GAME_OVER:
            self.update_game_over()
            return
        elif self.state == State.STAGE_CLEAR:
            self.update_stage_clear()

        self.background.update()

        sprites_update(self.powerups)
        sprites_update(self.player_shots)
        sprites_update(self.enemies)
        sprites_update(self.bosses)
        sprites_update(self.enemy_shots)

        if self.check_stage_clear:
            self.check_stage_clear = False
            if len(self.bosses) == 0:
                self.stage_clear_init()

        sprite_lists_collide(self.player_shots, self.enemies)
        sprite_lists_collide(self.player_shots, self.bosses)
        sprite_collide_list(self.player, self.powerups)
        sprite_collide_list(self.player, self.enemy_shots)
        sprite_collide_list(self.player, self.enemies)
        sprite_collide_list(self.player, self.bosses)

        sprites_update(self.explosions)

        if self.state == State.PLAY and self.player.remove:
            self.switch_state(State.PLAYER_DEAD)
            self.player_shots.clear()
    
    def draw(self):
        self.background.draw()

        if self.state != State.PLAYER_DEAD and \
            self.state != State.GAME_OVER:
            self.player.draw()

        sprites_draw(self.powerups)
        sprites_draw(self.player_shots)
        sprites_draw(self.enemies)
        sprites_draw(self.bosses)
        sprites_draw(self.explosions)
        sprites_draw(self.enemy_shots)

        self.hud.draw()

        if self.state == State.PAUSED:
            self.font.draw_text(104, 88, "PAUSED")
        elif self.state == State.GAME_OVER:
            self.font.draw_text(96, 88, "GAME OVER")
        elif self.state == State.STAGE_CLEAR:
            if self.game.game_vars.stage_num != FINAL_STAGE:
                if self.state_time > 60:
                    if self.game.game_vars.is_vortex_stage():
                        self.font.draw_text(80, 88, "LEAVING VORTEX")
                    else:
                        self.font.draw_text(80, 88, "ENTERING VORTEX")
    