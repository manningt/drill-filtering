from dups_detected_by_chksum_list import dups_list

from drill_titles_no_dups import drill_list
drill_titles_no_dups_list = []
for item in drill_list:
   if item["id"] not in dups_list:
      drill_titles_no_dups_list.append(item)

write_no_dups_dict = True
if write_no_dups_dict:
   MyFile=open('drill_titles_no_dups-2.py','w')
   MyFile.write("drill_list = [\\\n")
   for drill_dict in drill_titles_no_dups_list:
      MyFile.write(str(drill_dict)+",\\\n")
   MyFile.write("]")
   # MyFile.write(str(drill_titles_no_dups_list))
   MyFile.close()
