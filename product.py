def product(list):
  result = 1 
  for num in list:
    result *= num 
  return result 
  
print(product([1,2]))