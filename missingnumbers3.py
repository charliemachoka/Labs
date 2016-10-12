def find_missing(list1,list2):
  
  find = 0
  if len(list1) > len(list2):
    diff = set(list1) - set(list2)
    find = diff.pop()
    return find
    
  elif len(list1) < len(list2):
    diff = set(list2) - set(list1)
    find = diff.pop()
    return find
    
  return (0)
