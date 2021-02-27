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
from drill_titles_no_dups import drill_list

if __name__ == "__main__":
   # fname = "DRL973"
   DRILL_PATH = '/Users/tom/Documents/Projects/Boomer/infrastructure/drills/'
   drill_list = [{'id': '000', 'name': 'speed test'},\
                  {'id': '001', 'name': '2-line groundstroke footwork'}]

   for i, drill in enumerate(drill_list):
      fname = "DRL" + drill["id"]
      parse_error_string, drill_name, drill_desc, intro_audio, ball_list \
         = parse_drill_file(DRILL_PATH + fname + ".CMP")
      if parse_error_string is not None:
         print("File {}: Parse {}".format(fname, parse_error_string))
      elif len(ball_list) == 0:
         print("File {} Error: no balls configured ".format(fname))

      

      stats = {}
      for label in BALL_CFG_LABELS:
         stats[label[:-2]] = {"count": 0, "min": 0,"max": 0}

      for j, ball_cfg in enumerate(ball_list):
         for label in BALL_CFG_LABELS:
            if label[:-2] in ball_cfg:
               stats[label[:-2]]["count"] += 1
               if ball_cfg[label[:-2]]
      
      drill_list[i]["stats"] = stats

   for i, drill in enumerate(drill_list):
      print("{}".format(drill))


   # ----- write reports/files:
   write_file = False
   if write_file:
      MyFile=open("drill_analysis_report.txt",'w')
      # escaped quotes around the string make it so the commas aren't handled as column delimiters

      MyFile.write("NAME,\"{}\"\n".format(drill_name))
      MyFile.write("DESC,\"{}\"\n".format(drill_desc))
      MyFile.write("INTRO,{}\n".format(intro_audio))
      # write header row
      csv_line = ","
      for i in range(len(ball_list)):
         csv_line += "{}".format(i+1)
         if i < len(ball_list)-1:
            csv_line += ","
         else:
            csv_line += "\n"
      MyFile.write(csv_line)
      # write other row for each drill
      for label in BALL_CFG_LABELS:
         label_has_values = False
         csv_line = label[:-2] + ","
         for i, ball_cfg in enumerate(ball_list):
            if label[:-2] in ball_cfg:
               csv_line += ball_cfg[label[:-2]]
               label_has_values = True
            if i < len(ball_list)-1:
               csv_line += ","
            else:
               csv_line += "\n"
         if label_has_values:
            MyFile.write(csv_line)
      MyFile.close()

   print("'{}' had {} ball configurations".format(drill_name, len(ball_list)))