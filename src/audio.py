
import json
from enum import IntEnum, auto

import pyxel as px

# Title screen music is all channels (0-3)
# In-stage music is channels 0-2
SOUND_CHANNEL = 3
# Sounds (not channels) 0-3 used when music loaded from JSON.
class SoundType(IntEnum):
    RESERVED_MUSIC_0 = 0
    RESERVED_MUSIC_1 = auto()
    RESERVED_MUSIC_2 = auto()
    RESERVED_MUSIC_3 = auto()
    ##
    EXPLODE_SMALL = auto()
    BLIP = auto()
    WEAPON_POWERUP = auto()
    LIFE_POWERUP = auto()
    BOMB_POWERUP = auto()

SND_PRIORITY = {
    SoundType.EXPLODE_SMALL : 5,
    SoundType.BLIP : 4,
    SoundType.WEAPON_POWERUP : 10,
    SoundType.LIFE_POWERUP : 10,
    SoundType.BOMB_POWERUP : 10,
}

SOUND_CHANNEL_GAIN_DEFAULT = 0.125

last_sound_played = 0

def load_music(file):
    with open(f"assets/{file}", "rt") as fin:
        return json.loads(fin.read())
    
def play_music(music, doLoop=True, num_channels=4, theTick=None):
    for ch, sound in enumerate(music):
        px.sounds[ch].set(*sound)
        px.play(ch, ch, tick=theTick, loop=doLoop)
        if ch == num_channels-1: 
            break
        
def reset_music_gain(num_channels=4):
    for i in range(num_channels):
        px.channels[i].gain = SOUND_CHANNEL_GAIN_DEFAULT

def fade_out_music(gain, num_channels=4):
    if gain > 0:
        gain = max(0, gain - 0.001)
        if gain == 0:
            stop_music(num_channels)
        else:
            for i in range(num_channels):
                px.channels[i].gain = gain
    return gain
        
def stop_music(num_channels=4):
    for i in range(num_channels):
        px.stop(i)
        
def is_music_playing():
    return px.play_pos(0) is not None

def play_sound(sound, doLoop=False, priority=False):
    global last_sound_played
    if px.play_pos(SOUND_CHANNEL) is None:
        px.play(SOUND_CHANNEL, snd=sound, loop=doLoop)
        last_sound_played = sound
    else:
        if priority or SND_PRIORITY[sound] >= SND_PRIORITY[last_sound_played]:
            px.play(SOUND_CHANNEL, snd=sound, loop=doLoop)
            last_sound_played = sound

def stop_sound():
    px.stop(SOUND_CHANNEL)
