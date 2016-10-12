class BinarySearch(list):
   
    def __init__(self, a, b, *args):
        
        list.__init__(self, *args)
        self.l_length = a
        self.diff = b
        ultim = self.l_length * self.diff
        for num in range(self.diff, ultim + 1, self.diff):
            self.append(num)
    @property
    def length(self):
        return len(self)
   
    def search(self, value, sec = 0, first = None, count = 0):
       
        if not first:
            first = self.length - 1
       
        if value == self[sec]:
            return {'index': sec, 'count': count}
        
        elif value == self[first]:
            return {'index': first, 'count': count}
        middle = (sec + first) // 2
       
        if value == self[middle]:
            return {'index': middle, 'count': count}
       
        elif value > self[middle]:
            sec = middle + 1
       
        elif value < self[middle]:
            first = middle - 1
        
        if sec >= first:
            return {'index': -1, 'count': count}
        
        count += 1  
       
        return self.search(value, sec, first, count)
