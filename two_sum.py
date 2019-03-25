# write a function that returns the indices of array elements that sum to 0
def two_sum(arr1, arr2):
  result = []
  for i in range(len(arr1)): 
    for j in range(len(arr2)):
      if arr1[i] + arr2[j] == 0:
        result.append([i,j]) 
  return result 

print(two_sum([1,2,3], [-1,2,3]))