from score_method_mapping import boomer2_score_method_mapping
from boomer_2_score_methods import boomer2_score_methods

usage_count = [0] * len(boomer2_score_methods)
# print(f"number of boomer2 score methods is {len(boomer2_score_methods)}")

for value in boomer2_score_method_mapping.values():
   if value != '':
      index = boomer2_score_methods.index(value)
   usage_count[index] += 1

print(f"usage_count: {usage_count}")

for index, count in enumerate(usage_count):
   if count == 0:
      print(f"{boomer2_score_methods[index]}, ", end='')

print("were not used.")

