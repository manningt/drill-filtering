#opens and parses a drill file
#returns (parse_error_string, drill_name, drill_desc, intro_audio, ball_list)
import re
from drill_file_defines import *
from drill_file_defines_adjunct import *

# value = SHOTTYPE_VALUE_LIST[SHOTTYPE_NAME_LIST.index("CHIP")]
# print(value)

def parse_drill_file(fname):
   drill_name = None
   drill_desc = None
   intro_audio = None
   ball_list = []

   with open(fname, "r") as f:
      line = f.readline().rstrip()
      if (line.find(NAME_DF) > -1):
         drill_name = line[len(NAME_DF):]
      else:
         return "Err: Missing {}".format(NAME_DF)
         # print("File {}: Missing Name".format(fname))
         # sys.exit(0)

      # collect description
      line = f.readline()
      # if not re.match(DESC_START, line, re.IGNORECASE):
      if DESC_START in line:
         drill_desc = ""
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
            return "Err: Missing {}".format(DESC_END)

      # collect optional intro audio
      line = ""
      #skip blank lines
      while (len(line) < 2):
         line = f.readline()
         if len(line) == 0:
            return (None, drill_name, drill_desc, intro_audio, ball_list)
            # print("drill_eof before ball configs found")
            # sys.exit()
      if re.match(INTRO_AUDIO_DF, line, re.IGNORECASE):
         intro_audio = line[len(INTRO_AUDIO_DF):].strip()

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
         if BALL_DF in line:
            if len(ball_params) > 0:
               ball_list.append(ball_params)
            ball_params = {}
         else:
            line = line.strip()
            for label in BALL_CFG_LABELS:
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

   return (None, drill_name, drill_desc, intro_audio, ball_list)