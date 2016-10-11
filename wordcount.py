def words(word):
  worddict = {}
  sword = word.split()
  
  for newword in sword:
    if newword in worddict:
      worddict[newword] += 1
    else:
      worddict[newword] = 1
      
  return worddict

  
