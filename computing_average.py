grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  sum = 0 
  for score in scores:
    sum += score 
  return sum

print(grades_sum(grades))

def grades_average(grades_input):
  temp = grades_sum(grades_input) 
  return temp / float(len(grades_input))

print(grades_average(grades))