def replicate_iter(times, data):
    if((not isinstance(times, int)) or (not isinstance(data, (int, str)))):
            raise ValueError("Invalid arguments")
    while(times <= 0):
            return []
    else:
            array = []
            for x in range(times):
                    array.append(data)
            return array


def replicate_recur(times, data):
    if((not isinstance(times, int)) or (not isinstance(data, (int, str)))):
            raise ValueError("Invalid arguments")
    while(times <= 0):
            return []
    else:
            return ([data] + replicate_recur((times - 1), data)) 
