import sys
from drill_list_w_details import drill_list
from score_method_mapping import boomer2_score_method_mapping

def elevation_mapping(elevation):
   ret_val = 45
   if elevation == 0:
      ret_val = 4
   elif elevation == 1:
      ret_val = 1
   elif elevation < 89:
      ret_val = elevation//2
   return ret_val

for drill in drill_list:
   filename = f"../drills_csv/DRL{drill['id']}.csv"
   try:
      f = open(filename, "w")
   except OSError:
      print(f"Could not open file: {filename}")
      sys.exit()

   f.write(f"\"{drill['name']}\"\n")
   f.write(f"\"{drill['desc']}\"\n")
   if drill['audio'] is not None:
      f.write(f"{drill['audio']}")
   f.write("\n")
   # boomer 1 row ordering: dshot+i,dslev+i,drots+i,dcost+i,ddel+i,dinstr+i,dspeed+i,dspin+i,delev+i);
   ball_params=['SHOT_TYPE', 'ROTARY_TYPE', 'DELAY', 'SCORE_METHOD', 'LEVEL', 'COMMENT', 'SPEED', 'ELEVATION', 'SPIN']

   # write header row; note: intentionally putting in a blank column 'A' for each ball so that they are offset
   #   from name, desc, audit hence each parameter write starts with a , to make a new column.
   for param in ball_params:
      f.write(f",{param}")
   f.write("\n")

   ball_params[5] = 'AUDIO' # Drew format used AUDIO instead of COMMENT or INSTRUCTION

   for ball in drill['balls']:
      for param in ball_params:
         if param in ball:
            if (param is "SCORE_METHOD"):
               f.write(f",{boomer2_score_method_mapping[int(ball[param])]}")
            elif (param is "ELEVATION"):
               f.write(f",{elevation_mapping(int(ball[param]))}")
            else:
               f.write(f",{ball[param]}")
         else:
            f.write(f",")
      f.write("\n")

   if drill['id'] == '018':
      print(f"stopped at drill: {drill['id']}")
      sys.exit()

   f.close()
