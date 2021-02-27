# determine which dups to remove based on diff output
import re
import sys
# example line: Files DRL058.CMP and DRL548.CMP are identical

identical_drills = []
audit_list = []
# previous_drill_pair = []
with open('dups_diff-output.txt', 'r') as f:
   line = f.readline()
   while line:
      drill_pair = re.findall(r"DRL\d\d\d\.CMP", line)
      # drill_pair: ['DRL058.CMP', 'DRL548.CMP']
      audit_string = "{} {}: ".format(drill_pair[0], drill_pair[1])
      if "identical" in line:
         identical_drills.append(drill_pair[1][3:6])
         audit_string += "delete {}".format(drill_pair[1][3:6])
         # if len(previous_drill_pair) == 0 or drill_pair[0] != previous_drill_pair[1] or \
         #    drill_pair[0] == identical_drills[-1]:
         #    previous_drill_pair = drill_pair
      else:
         audit_string += "differ"
      audit_list.append(audit_string)
      line = f.readline()

print("number of drills to remove: {}".format(len(identical_drills)))

write_audit = False
if write_audit:
   MyFile=open('remove-audit.txt','w')
   for item in audit_list:
      MyFile.write(item + "\n")
   MyFile.close()

from drill_titles_no_new import drill_list
drill_titles_no_dups_list = []
for item in drill_list:
   if item["id"] not in identical_drills:
      drill_titles_no_dups_list.append(item)
print("Number of drill names w/ dups removed: {}".format(len(drill_titles_no_dups_list)))

write_no_dups_dict = True
if write_no_dups_dict:
   MyFile=open('drill_titles_no_dups.py','w')
   MyFile.write("drill_list = ")
   MyFile.write(str(drill_titles_no_dups_list))
   MyFile.close()

# i = 0
# for item in identical_drills:
#    print(item[3:6])
#    i += 1
#    if i > 8:
#       break
