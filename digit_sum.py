def digit_sum(n):
  n_str = str(n) 
  result = 0
  for char in n_str:
    result += int(char) 
  return result 

print(digit_sum(1234))