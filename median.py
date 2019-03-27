def median(list):
  list = sorted(list)
  midpoint = int((len(list) / 2))
  print(midpoint)
  if (len(list) % 2 == 0):
    first = list[midpoint-1] 
    second = list[midpoint] 
    return (first + second) / 2
  else:
    return list[midpoint]






print(median([4, 5, 5, 4]))