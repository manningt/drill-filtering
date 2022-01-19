#!/usr/bin/env python3

import sys
import os
from drill_file_defines import *
from drill_file_defines_adjunct import *
from drill_file_parser import parse_drill_file

'''
Boomer 1 column order: dshot+i,dslev+i,drots+i,dcost+i,ddel+i,dinstr+i,dspeed+i,dspin+i,delev+i);
'''

if __name__ == "__main__":
   import argparse
   parser = argparse.ArgumentParser(description='Open drill file, parse and write .csv file')
   parser.add_argument(dest='drill_file', type=str, nargs='?', help='filename of drill file')
   args = parser.parse_args()

   if args.drill_file is None:
      fname = input("Drill filename: ").rstrip()
   else:
      fname = args.drill_file

   if ".CMP" in fname:
      fname = fname[:-4]
   # fname = "DRL973"
   DRILL_PATH = '/Users/tom/Documents/Projects/Boomer/Boomer_drills/'
   if not os.path.isfile(DRILL_PATH + fname + ".CMP"):
      print("File does not exist: {}.CMP".format(DRILL_PATH + fname))
      sys.exit(1)
   
   parse_error_string, drill_name, drill_desc, intro_audio, ball_list \
      = parse_drill_file(DRILL_PATH + fname + ".CMP")
   if parse_error_string is not None:
      print("File {}: Parse {}".format(fname, parse_error_string))
      sys.exit(1)
   elif len(ball_list) == 0:
      print("File {} Error: no balls configured ".format(fname))
      sys.exit(1)

   # ----- write reports/files:
   print_balls = False
   if print_balls:
      print("name: {}".format(drill_name))
      print("desc: {}".format(drill_desc))
      print("audio: {}".format(intro_audio))
      for i, ball_cfg in enumerate(ball_list):
         print("Ball {}: {}".format(i, ball_cfg))
         if i > 2:
            break

   write_file = True
   if write_file:
      MyFile=open(fname + ".csv",'w')
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