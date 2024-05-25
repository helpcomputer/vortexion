
from enemy_a import EnemyA
from enemy_b import EnemyB
from enemy_c import EnemyC
from enemy_d import EnemyD
from enemy_e import EnemyE
from enemy_f import EnemyF
from enemy_g import EnemyG
from enemy_h import EnemyH
from enemy_i import EnemyI
from enemy_j import EnemyJ # Defence Turret for Boss
from enemy_k import EnemyK # Boss 1 circle
from enemy_l import EnemyL # Boss 2: big leaves
from enemy_m import EnemyM # Boss 3: eye
from enemy_n import EnemyN
from enemy_o import EnemyO
from enemy_p import EnemyP

ENEMY_SPAWN_TILE_X = {
    0 : EnemyA, 
    16 : EnemyB, 
    32 : EnemyC, 
    48 : EnemyD, 
    64 : EnemyE, 
    80 : EnemyF, 
    96 : EnemyG, 
    112 : EnemyH, 
    128 : EnemyI,
    144 : EnemyJ,
    208 : EnemyN,
    224 : EnemyO,
    240 : EnemyP,
}

ENEMY_BOSS_SPAWN_TILE_X = {
    160 : EnemyK,
    176 : EnemyL,
    192 : EnemyM,
}

ENEMY_SPAWN_TILE_INDEX_Y = 10

def create(state, tile_x, x, y):
    if tile_x in ENEMY_BOSS_SPAWN_TILE_X:
        f = ENEMY_BOSS_SPAWN_TILE_X[tile_x]
        state.add_boss(f(state, x, y))
    elif tile_x in ENEMY_SPAWN_TILE_X:
        f = ENEMY_SPAWN_TILE_X[tile_x]
        state.add_enemy(f(state, x, y))
    