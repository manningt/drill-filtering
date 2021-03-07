#!/usr/bin/env python3

'''
add to drill_list:
{'id': '000', 'name': 'speed test', 'ball_count': 5, "stats": {\
   {LEVEL_DF: {"count": 1, "min": 1, "max": 1, "easy": 1, "hard": 1, "same": 1}}
   {DELAY_DF: {"count": 1, "min": 1, "max": 1}}}
   

BALL_CFG_LABELS = [SHOTTYPE_DF, LEVEL_DF, ROTARY_TYPE_DF, SCORE_METHOD_DF, DELAY_DF,\
   SPEED_DF, SPIN_DF , ELEVATION_DF, AUDIO_DF]
'''

import sys
import os
from drill_file_defines import *
from drill_file_defines_adjunct import *
from drill_file_parser import parse_drill_file
from drill_list_w_details import drill_list

if __name__ == "__main__":

   analyze_desc = True
   if analyze_desc:
      w_desc = []
      w_desc_none = []
      wo_desc = []
      for i, drill in enumerate(drill_list):
         if drill['desc'] is None:
            w_desc_none.append(drill['id'])
         elif len(drill['desc']) > 1:
            w_desc.append(drill['id'])
         else:
            wo_desc.append(drill['id'])
      print("---\nDrills without a description block: {}".format(w_desc_none))
      print("Drills with a description:\n{}".format(w_desc))
      print("\n{} drills do not have a description.\n".format(len(wo_desc)))


   analyze_levels = False
   if analyze_levels:
      from enum import IntEnum
      class difficulty(IntEnum):
         same = 0
         easy = 1
         hard = 2

      # word_level means easy, hard, same
      single_word_level_count = [0] * 3
      single_word_level_list = []
      for i in range(0,3):
         single_word_level_list.append([])
      numeric_level_count = [0] * 14
      multiple_level_count = 0
      no_level_count = 0
      sets_list = []
      sets_count = []
      drills_per_set = [] # a list of lists
      for i, drill in enumerate(drill_list):
         level_set = set()
         for j, ball_cfg in enumerate(drill['balls']):
            level_set.add(ball_cfg[LEVEL_DF[:-2]].lower())
         if len(level_set) == 0:
            no_level_count += 1
         elif len(level_set) == 1:
            if 'easy' in level_set:
               single_word_level_count[difficulty.easy] += 1
               single_word_level_list[difficulty.easy].append(drill['id'])
            if 'hard' in level_set:
               single_word_level_count[difficulty.hard] += 1
               single_word_level_list[difficulty.hard].append(drill['id'])
            if 'same' in level_set:
               single_word_level_count[difficulty.same] += 1
         else:
            multiple_level_count += 1
            new_set = True
            for s in range(len(sets_list)):
               if sets_list[s] == level_set:
                  sets_count[s] += 1
                  drills_per_set[s].append(drill['id'])
                  new_set = False
            if new_set:
               sets_list.append(level_set)
               sets_count.append(1)
               drills_per_set.append([(drill['id'])])

      print("---\nOut of {} drills:".format(len(drill_list)))
      print("Exclusively same: {}  easy: {}  hard: {}".format(single_word_level_count[difficulty.same], \
         single_word_level_count[difficulty.easy], single_word_level_count[difficulty.hard]))
      print("List of exclusively hard: {}    List of exclusively easy: {}".format(single_word_level_list[difficulty.hard], \
         single_word_level_list[difficulty.easy]))
      print("No levels: {}  Multiple levels {}".format(no_level_count , multiple_level_count ))
      for s in range(len(sets_list)):
         print("Set: {} used in {} drills; ids: {}".format(sets_list[s], sets_count[s], drills_per_set[s]))
      

   analyze_scoring_methods = False
   if analyze_scoring_methods:
      drills_w_score_methods_id = []
      drills_w_score_methods_name = []
      drills_w_score_methods_set = []
      for i, drill in enumerate(drill_list):
         score_set = set()
         for j, ball_cfg in enumerate(drill['balls']):
            score_set.add(ball_cfg[SCORE_METHOD_DF[:-2]])
         drills_w_score_methods_id.append(drill["id"])
         drills_w_score_methods_name.append(drill["name"])
         drills_w_score_methods_set.append(score_set)

      fname = "score_methods"
      MyFile=open(fname + ".csv",'w')
      MyFile.write("id,name,methods\n")
      for j in range(len(drills_w_score_methods_id)):
         MyFile.write("{},\"{}\",\"{}\"\n".format(drills_w_score_methods_id[j], \
            drills_w_score_methods_name[j], drills_w_score_methods_set[j] ))
      MyFile.close()


   analyze_custom_and_ball_counts = False
   if analyze_custom_and_ball_counts:
      THREE_BALL_COUNT = 3
      drills_w_less_than_3_balls_id = []
      drills_w_less_than_3_balls_name = []
      FOUR_BALL_COUNT = 4
      drills_w_less_than_4_balls_id = []
      drills_w_less_than_4_balls_name = []
      drills_w_custom_balls = []
      drills_w_custom_ball_incomplete = []
      for i, drill in enumerate(drill_list):
         if len(drill["balls"]) < THREE_BALL_COUNT:
            drills_w_less_than_3_balls_id.append(drill["id"])
            drills_w_less_than_3_balls_name.append(drill["name"])
         elif len(drill["balls"]) < FOUR_BALL_COUNT:
            drills_w_less_than_4_balls_id.append(drill["id"])
            drills_w_less_than_4_balls_name.append(drill["name"])
         for j, ball_cfg in enumerate(drill["balls"]):
            if CUSTOM_NAME_BALLTYPE == ball_cfg[SHOTTYPE_DF[:-2]]:
               if j == 0:
                  drills_w_custom_balls.append(drill["id"])
               if SPEED_DF[:-2] not in ball_cfg or \
                  SPIN_DF[:-2] not in ball_cfg or \
                  ELEVATION_DF[:-2] not in ball_cfg:
                  print("custom ball doesn't have all params configurated: Drill: {}".format(drill["id"]))
                  sys.exit(0)

      print("\n--- Drills with less than {} balls".format(THREE_BALL_COUNT))
      for j in range(len(drills_w_less_than_3_balls_id)):
         print("{} {}".format(drills_w_less_than_3_balls_id[j], drills_w_less_than_3_balls_name[j]))
      print("--- Drills with less than {} balls".format(FOUR_BALL_COUNT))
      for j in range(len(drills_w_less_than_4_balls_id)):
         print("{} {}".format(drills_w_less_than_4_balls_id[j], drills_w_less_than_4_balls_name[j]))
      print("Number of drills with custom balls: {}".format(len(drills_w_custom_balls)))

