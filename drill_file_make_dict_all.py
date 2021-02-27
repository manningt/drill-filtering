#!/usr/bin/env python3

'''
add the rest of the drill file contents to the dictionary for a drill:
{'id': '000', 'name': 'speed test', 'desc': "asfsf", "balls": [dict per ball]

'''
import sys
import os
from drill_file_parser import parse_drill_file

# drill_list = [{'id': '000', 'name': 'speed test'},\
#                {'id': '001', 'name': '2-line groundstroke footwork'}]
from drill_titles_no_dups import drill_list

if __name__ == "__main__":
   # fname = "DRL973"
   DRILL_PATH = '/Users/tom/Documents/Projects/Boomer/infrastructure/drills/'
   for i, drill in enumerate(drill_list):
      fname = "DRL" + drill["id"]
      parse_error_string, drill_name, drill_desc, intro_audio, ball_list \
         = parse_drill_file(DRILL_PATH + fname + ".CMP")
      # if len(rc) < 5:
      #    print("File {}: Parse {}".format(fname, rc[0]))
      #    sys.exit(1)
      # else:
      #    parse_error_string = rc[0]
      #    drill_desc = rc[2]
      #    intro_audio = rc[3]
      #    ball_list = rc[4]
         
      if parse_error_string is not None:
         print("File {}: Parse {}".format(fname, parse_error_string))
         sys.exit(1)
      elif len(ball_list) == 0:
         print("File {} Error: no balls configured ".format(fname))
      else:
         drill_list[i]["desc"] = drill_desc
         drill_list[i]["audio"] = intro_audio
         drill_list[i]["balls"] = ball_list

   write_full_drill_dict = True
   if write_full_drill_dict:
      MyFile=open('drill_list_w_details.py','w')
      MyFile.write("drill_list = [\\\n")
      for drill_dict in drill_list:
         MyFile.write(str(drill_dict)+",\\\n")
      MyFile.write("]")
      MyFile.close()
