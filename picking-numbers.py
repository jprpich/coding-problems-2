# write a function that picks only even numbers
def pickingNumbers(a):
  evens = [] 
  for number in a: 
    if number % 2 == 0:
      evens.append(number) 
  return evens 
  
print(pickingNumbers([4, 6, 5, 3, 3, 1]))