"""this tedious module is for printing nestd lists"""
def print_lol(the_list, indent):
  for list_item in the_list:
    if isinstance(list_item, list):
      print_lol(list_item, indent + 1)
    else:
      for tabs in range(indent):
        print ("\t", end='')
      print(list_item)

