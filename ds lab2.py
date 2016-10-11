def manipulate_data(mylist):
    mynewlist = []
    mycount = 0
    mysum = 0
    if type(mylist) != list:
      return 'Only lists allowed'
    else:
      for i in mylist:
        if i >= 0:
          mycount += 1          
        elif i < 0:
          mysum += i
    mynewlist.append(mycount)
    mynewlist.append(mysum)
    return mynewlist
