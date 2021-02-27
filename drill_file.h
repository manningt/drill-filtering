// defines for DRLxxx.CMP file access
#ifdef __cplusplus
extern "C" {
#endif

// #pragma once
#ifndef drill_file_h
#define drill_file_h

//-=-=- start of exported defines
//fields:
#define DF_NAME "NAME: "
#define DESC_START "[DESCRIPTION_START]"
#define DESC_END "[DESCRIPTION_END]"
#define DF_INTRO_AUDIO "INTRO_AUDIO: "
#define DF_BALL "[BALL]"
#define DF_SHOT_TYPE "SHOT_TYPE: "
#define DF_LEVEL "LEVEL: "
#define DF_ROTARY_TYPE "ROTARY_TYPE: "
#define DF_SCORE_METHOD "SCORE_METHOD: "   // drill_balls[ball_number].cost
#define DF_DELAY "DELAY: "
#define DF_SPEED "SPEED: "
#define DF_SPIN "SPIN: "
#define DF_ELEVATION "ELEVATION: "        // drill_balls[ball_number].y_ang
#define DF_AUDIO "AUDIO: "

// BALLTYPE_, ROTTYPE_ and LEVEL_ in calc_ball.h

#define SERVE_NAME_SHOTTYPE "SERVE"
#define DROP_NAME_SHOTTYPE "DROP"
#define FLAT_NAME_SHOTTYPE "FLAT"
#define HEAVY_NAME_SHOTTYPE "HEAVY"
#define CHIP_NAME_SHOTTYPE "CHIP"
#define LOB_NAME_SHOTTYPE "LOB"
#define TOPSPIN_NAME_SHOTTYPE "TOPSPIN"
#define PASS_NAME_SHOTTYPE "PASS"
#define NONE_NAME_SHOTTYPE "NONE"
#define CUSTOM_NAME_SHOTTYPE "CUSTOM"
#define RAND_GROUND_NAME_SHOTTYPE "RAND_GROUND"
#define RAND_NET_NAME_SHOTTYPE "RAND_NET"

#define SERVE_VALUE_SHOTTYPE 0
#define DROP_VALUE_SHOTTYPE 4
#define FLAT_VALUE_SHOTTYPE 8
#define HEAVY_VALUE_SHOTTYPE 12
#define CHIP_VALUE_SHOTTYPE 16
#define LOB_VALUE_SHOTTYPE 20
#define TOPSPIN_VALUE_SHOTTYPE 24
#define PASS_VALUE_SHOTTYPE 28
#define NONE_VALUE_SHOTTYPE 32
#define CUSTOM_VALUE_SHOTTYPE 36
#define RAND_GROUND_VALUE_SHOTTYPE 40
#define RAND_NET_VALUE_SHOTTYPE 44

#define F4_NAME_ROTARY "F4"
#define F3_NAME_ROTARY "F3"
#define F2_NAME_ROTARY "F2"
#define F1_NAME_ROTARY "F1"
#define CENTER_NAME_ROTARY "CENTER"
#define B1_NAME_ROTARY "B1"
#define B2_NAME_ROTARY "B2"
#define B3_NAME_ROTARY "B3"
#define B4_NAME_ROTARY "B4"
#define RAND_NAME_ROTARY "RAND"
#define F5_NAME_ROTARY "F5"
#define B5_NAME_ROTARY "B5"
#define RANDFH_NAME_ROTARY "RANDFH"
#define RANDBH_NAME_ROTARY "RANDBH"
#define R2_NAME_ROTARY "R2"
#define R3_NAME_ROTARY "R3"
#define INV_NAME_ROTARY "INV"

#define F4_VALUE_ROTARY 0
#define F3_VALUE_ROTARY 1
#define F2_VALUE_ROTARY 2
#define F1_VALUE_ROTARY 3
#define CENTER_VALUE_ROTARY 4
#define B1_VALUE_ROTARY 5
#define B2_VALUE_ROTARY 6
#define B3_VALUE_ROTARY 7
#define B4_VALUE_ROTARY 8
#define RAND_VALUE_ROTARY 9
#define F5_VALUE_ROTARY 10
#define B5_VALUE_ROTARY 11
#define RANDFH_VALUE_ROTARY 12
#define RANDBH_VALUE_ROTARY 13
#define R2_VALUE_ROTARY 14
#define R3_VALUE_ROTARY 15
#define INV_VALUE_ROTARY 16

#define SAME_NAME_LEVEL "SAME"
#define EASY_NAME_LEVEL "EASY"
#define HARD_NAME_LEVEL "HARD"
#define SAME_VALUE_LEVEL 0
#define EASY_VALUE_LEVEL 1
#define HARD_VALUE_LEVEL 2

// to be added: min/max for:
// spin
// elevation == y.ang



//-=-=- end of exported defines

#endif //ifndef ipc_test_support_h

#ifdef __cplusplus
}
#endif