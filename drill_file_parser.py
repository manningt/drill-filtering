
DRILL_PATH = '/Users/tom/Documents/Projects/Boomer/infrastructure/drills/'

import re
import sys
from drill_file_defines import *
from drill_file_defines_adjunct import SHOTTYPE_VALUE_LIST, SHOTTYPE_NAME_LIST

# value = SHOTTYPE_VALUE_LIST[SHOTTYPE_NAME_LIST.index("CHIP")]
# print(value)

fname = "DRL001"
line_num = 1
drill_name = None
drill_desc = ""
intro_audio = "No intro audio"
ball_list = []
ball_cfg_labels = [DF_SHOT_TYPE, DF_LEVEL, DF_ROTARY_TYPE, DF_SCORE_METHOD, DF_DELAY,\
   DF_SPEED, DF_SPIN , DF_ELEVATION, DF_AUDIO]

with open(DRILL_PATH + fname + ".CMP", "r") as f:
   line = f.readline().rstrip()
   if (line.find(DF_NAME) > -1):
      drill_name = line[len(DF_NAME):]
   else:
      print("File {}: Missing Name".format(fname))
      sys.exit(0)

   # collect description
   line = f.readline()
   # if not re.match(DESC_START, line, re.IGNORECASE):
   if not DESC_START in line:
      print("File {}: Missing Description Start".format(fname))
      sys.exit(0)
   desc_line_num = 1
   desc_end_found = False
   while (desc_line_num < 7):
      line = f.readline().rstrip()
      # if re.match(DESC_END, line, re.IGNORECASE):
      if DESC_END in line:
         desc_end_found = True
         break
      elif len(line) > 0:
         drill_desc += line + " "
      desc_line_num += 1
   if not desc_end_found:
      print("File {}: Missing Description End".format(fname))
      sys.exit(0)

   # collect optional intro audio
   line = ""
   #skip blank lines
   while (len(line) < 2):
      line = f.readline()
      if len(line) == 0:
         print("drill_eof before ball configs found")
         sys.exit()
   if re.match(DF_INTRO_AUDIO, line, re.IGNORECASE):
      intro_audio = line[len(DF_INTRO_AUDIO):].strip()

   drill_eof = False
   line = ""
   #skip blank lines
   while (len(line) < 2):
      line = f.readline()
      if len(line) == 0:
         drill_eof = True

   readline_count = 1
   ball_params = {}
   # collect ball configs
   while not drill_eof:
      # print("Line {}: {}".format(readline_count, line))
      line = line.upper()
      if DF_BALL in line:
         if len(ball_params) > 0:
            ball_list.append(ball_params)
         ball_params = {}
      else:
         line = line.strip()
         for label in ball_cfg_labels:
            if label in line:
               ball_params[label[:-2]] = line[len(label):]
               break
      # read lines until next param
      line = ""
      while (len(line) < 2):
         line = f.readline()
         readline_count += 1
         if len(line) == 0:
            drill_eof = True
            break

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
   for label in ball_cfg_labels:
      csv_line = label[:-2] + ","
      for i, ball_cfg in enumerate(ball_list):
         if label[:-2] in ball_cfg:
            csv_line += ball_cfg[label[:-2]]
         if i < len(ball_list)-1:
            csv_line += ","
         else:
            csv_line += "\n"
      MyFile.write(csv_line)
   MyFile.close()

print("'{}' had {} ball configurations".format(drill_name, len(ball_list)))