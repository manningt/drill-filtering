
from drill_titles_no_dups import drill_list
import re
import copy

def get_index_positions(list_of_elems, element):
   # Returns the indexes of all occurrences of give element in the list- listOfElements
   index_pos_list = []
   index_pos = 0
   while True:
      try:
         # Search for item in list from indexPos to the end of list
         index_pos = list_of_elems.index(element, index_pos)
         # Add the index position in list
         index_pos_list.append(index_pos)
         index_pos += 1
      except ValueError as e:
         break
   return index_pos_list


volley_count = 0
v_count = 0
overhead_count = 0  #overhead plus volley
o_v_count = 0
ground_count = 0
net_count = 0
transition_count = 0
movement_count = 0  # movement, n-line
tiebreaker_count = 0
special_count = 0
uncategorized_count = 0
total_count = 0
sum_of_types = 0
uncategorized_list = []
ordered_names_list = []
duplicate_names_count = 0
duplicates_list = []
dup_pairs_list = []

easy_count = 0   # 1 gear, ball_count?
medium_count = 0   # 2nd, 3rd gear
hard_count = 0  # 4th gear
very_hard_count = 0 # 5th gear

# for key, value in drill_dict.items():
for i, item in enumerate(drill_list):
   total_count += 1
   current_name = item["name"]
   ordered_names_list.append(current_name.strip())
   if re.match(".*volley.*", current_name, re.IGNORECASE):
      volley_count += 1
   elif re.match(".* V .*", current_name) \
      and not re.match(".* O .*", current_name):
      v_count += 1
   elif re.match(".* V .*", current_name) \
      and re.match(".* O .*", current_name):
      o_v_count += 1
   elif re.match(".*overhead.*", current_name, re.IGNORECASE):
      overhead_count += 1
   elif re.match(".*ground.*", current_name, re.IGNORECASE):
      ground_count += 1
   elif re.match(".*net.*", current_name, re.IGNORECASE):
      net_count += 1
   elif re.match(".*transition.*", current_name, re.IGNORECASE):
      transition_count += 1
   elif re.match(".*movement.*", current_name, re.IGNORECASE):
      movement_count += 1
   elif re.match(".*line.*", current_name, re.IGNORECASE):
      movement_count += 1
   elif re.match(".*tie.*", current_name, re.IGNORECASE):
      tiebreaker_count += 1
   else:
      uncategorized_count += 1
      tmp = "{:<30}  DRL{}".format(current_name, item["id"])
      uncategorized_list.append(tmp)

print("--------")
print(" Volley: {}; V: {}\n Overhead: {}; O+V: {}\n Ground: {}\n Net {}\n \
Transition: {}\n Movement: {}\n Tiebreaker: {}\n Uncategorized: {}".\
   format(volley_count, v_count, overhead_count, o_v_count, \
      ground_count, net_count, transition_count, movement_count, \
         tiebreaker_count, uncategorized_count ))

sum_of_types += volley_count + v_count + overhead_count + o_v_count
sum_of_types += ground_count + net_count + transition_count + movement_count
sum_of_types += tiebreaker_count

# count duplicate drill names
sorted_names_list = copy.deepcopy(ordered_names_list)
sorted_names_list.sort()
for i, drill_name in enumerate(sorted_names_list):
   if (i>0) and (sorted_names_list[i] == sorted_names_list[i-1]):
      duplicate_names_count += 1
      if (i>1) and (sorted_names_list[i] == sorted_names_list[i-2]):
         pass
      else:
         #find drill numbers for this duplicate name
         dup_drill_name_index_list = get_index_positions(ordered_names_list, drill_name)
         for j, idx in enumerate(dup_drill_name_index_list):
            drill_dict = drill_list[idx]
            if j == 0:
               name_and_ids = "{:<30} in Drills: ".format(drill_dict["name"])
            name_and_ids += drill_dict["id"] + " "
            if j > 0:
               dup_pairs_list.append((previous_id, drill_dict["id"]))
            previous_id = drill_dict["id"]

         duplicates_list.append(name_and_ids)

print("Total: {}; SumOfTypes: {}; Uncategorized: {}; Missing: {}; Duplicates: {}".\
   format(total_count, sum_of_types, uncategorized_count, \
       (total_count - sum_of_types - uncategorized_count), duplicate_names_count))

print("--------")

write_files = False
if write_files:
   uncategorized_list.sort()
   MyFile=open('drills-uncategorized.txt','w')
   for item in uncategorized_list:
      MyFile.write(item + '\n')
   MyFile.close()

   MyFile=open('drills-duplicates.txt','w')
   for item in duplicates_list:
      MyFile.write(item + '\n')
   MyFile.close()

   MyFile=open('diff-dup-drills.sh','w')
   MyFile.write("#!/bin/bash\n")
   for pair in dup_pairs_list:
      diff_cmd = "diff -sq DRL{}.CMP DRL{}.CMP >> dups_diff.txt\n".format(pair[0], pair[1])
      MyFile.write(diff_cmd)
   MyFile.close()
