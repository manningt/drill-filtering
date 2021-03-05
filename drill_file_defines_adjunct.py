# makes lists for shottype and rotary lookups
from drill_file_defines import *

BALL_CFG_LABELS = [SHOTTYPE_DF, LEVEL_DF, ROTARY_TYPE_DF, SCORE_METHOD_DF, DELAY_DF,\
   SPEED_DF, SPIN_DF , ELEVATION_DF, AUDIO_DF]


BALLTYPE_NAME_LIST = [ \
SERVE_NAME_BALLTYPE, \
DROP_NAME_BALLTYPE, \
FLAT_NAME_BALLTYPE, \
HEAVY_NAME_BALLTYPE, \
CHIP_NAME_BALLTYPE, \
LOB_NAME_BALLTYPE, \
TOPSPIN_NAME_BALLTYPE, \
PASS_NAME_BALLTYPE, \
NONE_NAME_BALLTYPE, \
CUSTOM_NAME_BALLTYPE, \
RAND_GROUND_NAME_BALLTYPE, \
RAND_NET_NAME_BALLTYPE, \
]

BALLTYPE_VALUE_LIST = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44]

GROUND_BALLTYPES_NAMES = [TOPSPIN_NAME_BALLTYPE, PASS_NAME_BALLTYPE, FLAT_NAME_BALLTYPE, HEAVY_NAME_BALLTYPE, CHIP_NAME_BALLTYPE]
NET_BALLTYPES_NAMES = [LOB_NAME_BALLTYPE, PASS_NAME_BALLTYPE]
# CUSTOM_BALLTYPE has spin, speed and y_ang (ELEVATION) specified
# NON-CUSTOM BALLTYPE use LEVEL and BALLTYPE to lookup spin, speed & y_ang

# ROTARY F5 is -13 (forehand is the left side of Boomer,
#   aka 'Advantage court' - The receiver's left side service box, or the opponent's right for the server)
# ROTARY B5 is 13 (backhand is the right side of Boomer, aka 'Deuce court')
# ROTTYPE_R2 is random +/- 4   ROTTYPE_R3 is random +/- 6
# ROTTYPE_INV inverts the angle of the last shot