# generate a CSV with drill file #, name and chksum; chksum is to find dups
import hashlib
import copy
from drill_titles_no_dups import drill_list

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


DRILL_FILES_PATH ="/Users/tom/Documents/Projects/Boomer/infrastructure/drills/"
drill_chksum_list = []
ordered_id_list = []
sorted_drill_chksum_list = []
duplicates_list = []
ids_to_remove_list = []

# generate lists of IDs and chksums
for i, item in enumerate(drill_list):
   fname = DRILL_FILES_PATH
   fname += "DRL{}.CMP".format(item['id'])
   hash_md5 = hashlib.md5()
   with open(fname, "rb") as f:
      for chunk in iter(lambda: f.read(4096), b""):
         hash_md5.update(chunk)
   drill_chksum_list.append(hash_md5.hexdigest())
   ordered_id_list.append(item['id'])
 
   # drill_list[i]["chksum"] = hash_md5.hexdigest()

sorted_drill_chksum_list = copy.deepcopy(drill_chksum_list)
sorted_drill_chksum_list.sort()
for i, chksum in enumerate(sorted_drill_chksum_list):
   if (i>0) and (sorted_drill_chksum_list[i] == sorted_drill_chksum_list[i-1]):
      # print("dup chksum: {}".format(chksum))
      if (i>1) and (sorted_drill_chksum_list[i] == sorted_drill_chksum_list[i-2]):
         pass
      else:
         #find drill numbers for this duplicate chksum
         dup_chksum_index_list = get_index_positions(drill_chksum_list, chksum)
         # print("length of dup_chksum_list: {} ".format(len(dup_chksum_index_list)))
         chksum_and_ids = ""
         for j, idx in enumerate(dup_chksum_index_list):
            if j == 0:
               chksum_and_ids += "{}: ".format(chksum)
            else:
               ids_to_remove_list.append(ordered_id_list[idx])
            chksum_and_ids += ordered_id_list[idx] + " "
            
         duplicates_list.append(chksum_and_ids)


# print("Duplicate set count: {}".format(len(duplicates_list)))
for item in duplicates_list:
   print("{}".format(item))

print("\nIDs to remove list:\n{}\n".format(ids_to_remove_list))

write_csv_file = False
if write_csv_file:
   MyFile=open('drill-chksums.csv','w')   
   csv_line = "id,name,chksum\n"
   MyFile.write(csv_line)
   for item in drill_list:
      csv_line = "\'{},\"{}\",{}\n".format(item['id'], item['name'], item['chksum'])
      MyFile.write(csv_line)
   MyFile.close()