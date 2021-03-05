#!/usr/bin/env python3

'''
generates a report of differences between drills
'''

import sys
import os
from drill_file_defines import *
from drill_file_defines_adjunct import *
from drill_file_parser import parse_drill_file

DRILL_PATH = '/Users/tom/Documents/Projects/Boomer/infrastructure/drills/'

if __name__ == "__main__":
   import argparse
   parser = argparse.ArgumentParser(description='Open 2 drill file, parse and compare')
   parser.add_argument('-v', dest='verbose', nargs='?', help='print compares as well as miscompares')
   parser.add_argument(dest='file1', type=str, help='filename of drill file')
   parser.add_argument(dest='file2', type=str, help='filename of drill file')
   args = parser.parse_args()

   drill_file = [args.file1, args.file2]
   drill_name = []
   drill_desc = []
   intro_audio = []
   ball_list = []

   for i in range(len(drill_file)):
      if ".CMP" not in drill_file[i]:
         drill_file[i] = drill_file[i] + ".CMP"
      if not os.path.isfile(DRILL_PATH + drill_file[i]):
         print("File does not exist: {}.CMP".format(DRILL_PATH + drill_file[i]))
         sys.exit(1)
   
      parse_error_string, name, desc, intro_audio_t, ball_list_t \
         = parse_drill_file(DRILL_PATH + drill_file[i])

      if parse_error_string is not None:
         print("File {}: Parse {}".format(rill_file[i], parse_error_string))
         sys.exit(1)
      elif len(ball_list_t) == 0:
         print("File {} Error: no balls configured ".format(drill_file[i]))
         sys.exit(1)
      
      drill_name.append(name)
      drill_desc.append(desc)
      intro_audio.append(intro_audio_t)
      ball_list.append(ball_list_t)

   verbose = False
   if args.verbose is not None:
      verbose = True

   print("{:<9s}{:<14s}{:<32s}{:<32s}".format("","", drill_file[0], drill_file[1]))

   if drill_name[0] != drill_name[1]:
      print("{:<9s}{:<14s}{:<32s}{:<32s}".format("","name: ",drill_name[0], drill_name[1]))
   elif verbose:
      print("Drill NAMEs are the same: {}".format(drill_name[0]))

   ball_cfg_count = len(ball_list[0])
   if len(ball_list[0]) != len(ball_list[1]):
      print("{:<9s}{:<14s}{:<32d}{:<32d}".format("","ball_count: ", len(ball_list[0]), len(ball_list[1])))
      if len(ball_list[0]) > len(ball_list[1]):
         ball_cfg_count = len(ball_list[1])
   elif verbose:
      print("ball counts are the same: {}".format(len(ball_list[0])))

   # compare the dictionaries for each ball in the list
   ball_cfgs_w_diffs_count = 0
   for i in range(ball_cfg_count):
      common_keys = ball_list[0][i].keys() & ball_list[1][i].keys()
      ball_cfg_diff_found = False
      for k in common_keys:
         if ball_list[0][i][k] != ball_list[1][i][k]:
            print("ball-{:02d}: {:<14s}{:<32s}{:<32s}".format(i, k, ball_list[0][i][k], ball_list[1][i][k]))
            ball_cfg_diff_found = True

      if ball_cfg_diff_found:
         ball_cfgs_w_diffs_count += 1

      keys_in_0_not_in_1 = ball_list[0][i].keys() - ball_list[1][i].keys()
      keys_in_1_not_in_0 = ball_list[1][i].keys() - ball_list[0][i].keys()
      if len(keys_in_0_not_in_1) > 0 or len(keys_in_1_not_in_0) > 0:
         print("Keys in file1 not in 2: {}; not in file1 but in 2: {}".format(keys_in_0_not_in_1, keys_in_1_not_in_0))

   print("Out of {} ball_cfgs {} had differences.".format(ball_cfg_count, ball_cfgs_w_diffs_count))
