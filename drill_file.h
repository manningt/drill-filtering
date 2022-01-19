// defines for DRLxxx.CMP file access
#ifdef __cplusplus
extern "C" {
#endif

// #pragma once
#ifndef drill_file_h
#define drill_file_h

//-=-=- start of exported defines
//fields:
#define NAME_DF "NAME: "
#define DESC_START "[DESCRIPTION_START]"
#define DESC_END "[DESCRIPTION_END]"
#define INTRO_AUDIO_DF "INTRO_AUDIO: "
#define BALL_DF "[BALL]"
#define SHOTTYPE_DF "SHOT_TYPE: "
#define LEVEL_DF "LEVEL: "
#define ROTARY_TYPE_DF "ROTARY_TYPE: "
#define SCORE_METHOD_DF "SCORE_METHOD: "   // drill_balls[ball_number].cost
#define DELAY_DF "DELAY: "
#define SPEED_DF "SPEED: "
#define SPIN_DF "SPIN: "
#define ELEVATION_DF "ELEVATION: "        // drill_balls[ball_number].y_ang
#define AUDIO_DF "AUDIO: "

// the values for BALLTYE and ROTTYPE are in calc_ball.h, but not the names



// balltype aka SHOTTYPE and ROTTYPE from from calc_ball.h
#define BALLTYPE_SERVE 0
#define BALLTYPE_DROP 4
#define BALLTYPE_FLAT 8
#define BALLTYPE_HEAVY 12
#define BALLTYPE_CHIP 16
#define BALLTYPE_LOB 20
#define BALLTYPE_TOPSPIN 24
#define BALLTYPE_PASS 28
#define BALLTYPE_NONE 32
#define BALLTYPE_CUSTOM 36
#define BALLTYPE_RAND_GROUND 40
#define BALLTYPE_RAND_NET 44

//Ball Rotary Options
#define ROTTYPE_F4 0
#define ROTTYPE_F3 1
#define ROTTYPE_F2 2
#define ROTTYPE_F1 3
#define ROTTYPE_CENTER 4
#define ROTTYPE_B1 5
#define ROTTYPE_B2 6
#define ROTTYPE_B3 7
#define ROTTYPE_B4 8
#define ROTTYPE_RAND 9
#define ROTTYPE_F5 10
#define ROTTYPE_B5 11
#define ROTTYPE_RANDFH 12
#define ROTTYPE_RANDBH 13
#define ROTTYPE_R2 14
#define ROTTYPE_R3 15
#define ROTTYPE_INV 16

#define F4_NAME_ROTTYPE "F4"
#define F3_NAME_ROTTYPE "F3"
#define F2_NAME_ROTTYPE "F2"
#define F1_NAME_ROTTYPE "F1"
#define CENTER_NAME_ROTTYPE "CENTER"
#define B1_NAME_ROTTYPE "B1"
#define B2_NAME_ROTTYPE "B2"
#define B3_NAME_ROTTYPE "B3"
#define B4_NAME_ROTTYPE "B4"
#define RAND_NAME_ROTTYPE "RAND"
#define F5_NAME_ROTTYPE "F5"
#define B5_NAME_ROTTYPE "B5"
#define RANDFH_NAME_ROTTYPE "RANDFH"
#define RANDBH_NAME_ROTTYPE "RANDBH"
#define R2_NAME_ROTTYPE "R2"
#define R3_NAME_ROTTYPE "R3"
#define INV_NAME_ROTTYPE "INV"


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