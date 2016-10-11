def find_max_min(mylist):
  sortlist = sorted(mylist)
  if sortlist[0] == sortlist[-1]:
    return len(mylist)
  return [sortlist[0],sortlist[-1]]
