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

   analyze_scoring_methods = True
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

   analyze_all = False
   if analyze_all:
      for i, drill in enumerate(drill_list):
         stats = {}
         for label in BALL_CFG_LABELS:
            stats[label[:-2]] = {"count": 0, "min": 0,"max": 0}

         for j, ball_cfg in enumerate(ball_list):
            for label in BALL_CFG_LABELS:
               if label[:-2] in ball_cfg:
                  stats[label[:-2]]["count"] += 1
                  # if ball_cfg[label[:-2]]:
                  #    if type(var) is int:
         
         drill_list[i]["stats"] = stats

      for i, drill in enumerate(drill_list):
         print("{}".format(drill))



   # print("'{}' had {} ball configurations".format(drill_name, len(ball_list)))