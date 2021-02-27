
from drill_titles_no_dups import drill_list
import re

TEACHER_TAG = "Teacher"  # could be Coach/Teacher
PRO_TAG = "Pro"
PLAYERS_TAG = "Players" # 

GROUND_TAG = "Ground"
VOLLEY_TAG = "Volley"
OVERHEAD_TAG = "Overhead"
NET_TAG = "Net" #(overhead + volley) (O & V)
TRANSITION_TAG = "Transition"  # (baseline to short ball to volley)  15
MOVEMENT_TAG = "Movement"
WEAKER_TAG = "Weaker"
UNUSED_TAG = "Unused?"

tag_list = [TEACHER_TAG, PRO_TAG, PLAYERS_TAG, GROUND_TAG, VOLLEY_TAG, OVERHEAD_TAG, NET_TAG, \
   TRANSITION_TAG, MOVEMENT_TAG, WEAKER_TAG, UNUSED_TAG]

counts = {}

for i, item in enumerate(drill_list):
   if re.match("1.line .*", item["name"], re.IGNORECASE):
      drill_list[i][TEACHER_TAG] = 1
      drill_list[i][PRO_TAG] = 1
      drill_list[i][PLAYERS_TAG] = 1
   if re.match("2.line .*", item["name"], re.IGNORECASE):
      drill_list[i][TEACHER_TAG] = 1
      drill_list[i][PRO_TAG] = 1
   if re.match("3.line .*", item["name"], re.IGNORECASE):
      drill_list[i][TEACHER_TAG] = 1
      drill_list[i][PRO_TAG] = 1
   if re.match("4.line .*", item["name"], re.IGNORECASE):
      drill_list[i][PRO_TAG] = 1
   if re.match("5.line .*", item["name"], re.IGNORECASE):
      drill_list[i][UNUSED_TAG] = 1

   if re.match("tie.*", item["name"], re.IGNORECASE):
      drill_list[i][TRANSITION_TAG] = 1
   if re.match(".*net.*", item["name"], re.IGNORECASE):
      drill_list[i][NET_TAG] = 1
   if re.match(".*ground.*", item["name"], re.IGNORECASE):
      drill_list[i][GROUND_TAG] = 1
   if re.match(".*women.*", item["name"], re.IGNORECASE):
      drill_list[i][WEAKER_TAG] = 1
   if re.match(".*dub.*", item["name"], re.IGNORECASE):
      drill_list[i][WEAKER_TAG] = 1
   if re.match(".*up the line.*", item["name"], re.IGNORECASE):
      drill_list[i][WEAKER_TAG] = 1

   if re.match(".*overhead.*", item["name"], re.IGNORECASE):
      if re.match(".*volley.*", item["name"], re.IGNORECASE):
         drill_list[i][NET_TAG] = 1
      else:
         drill_list[i][OVERHEAD_TAG] = 1
   if re.match(".*volley.*", item["name"], re.IGNORECASE):
      if re.match(".*overhead.*", item["name"], re.IGNORECASE):
         pass # already counted under overhead match
      else:
         drill_list[i][VOLLEY_TAG] = 1

   if re.match(". O ", item["name"], re.IGNORECASE):
      if re.match(". V .*", item["name"], re.IGNORECASE):
         drill_list[i][NET_TAG] = 1
      else:
         drill_list[i][OVERHEAD_TAG] = 1
   if re.match(". V *", item["name"], re.IGNORECASE):
      if re.match(". O .*", item["name"], re.IGNORECASE):
         pass # already counted under overhead match
      else:
         drill_list[i][VOLLEY_TAG] = 1
   
print("total drill count: {}".format(len(drill_list)))

counts = {}
for tag in tag_list:
   counts[tag] = 0

write_file = True
if write_file:
   MyFile=open('drills.csv','w')
   # write header (1st row)
   csv_line = "id,name,"
   for i, tag in enumerate(tag_list):
      csv_line += tag
      if i < (len(tag_list)-1):
         csv_line += ","
   csv_line += "\n"
   MyFile.write(csv_line)
   # write other row for each drill
   for item in drill_list:
      csv_line = "\'{0},\"{1}\",".format(item['id'], item['name'])
      for i, tag in enumerate(tag_list):
         if tag in item:
            counts[tag] += 1
            if isinstance(item[tag], int):
               csv_line += str(item[tag])
            else:          
               csv_line += item[tag]
         if i < (len(tag_list)-1):
            csv_line += ","
      csv_line += "\n"
      MyFile.write(csv_line)
   MyFile.close()

   count_str = ""
   for tag in tag_list:
      count_str += "{}: {}  ".format(tag, counts[tag])
   print(counts)