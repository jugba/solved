"""
You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.
"""

def maximum_product_of_three(lst):
  size = len(lst)
  max_p = float('-inf')
  for i, val in enumerate(lst):
    if i + 1 < size:
      a = lst[i]
      b = lst[i+1]
      for j in range(0,i):
        t = a * b * lst[j]
        if t > max_p:
          max_p = t
      for k in range(i+2, size):
        t = a * b * lst[k]
        if t > max_p:
          max_p = t 
  return max_p

def maximum_two(nums):
  sorted_nums = nums.sort()
  largest_three = sorted_nums[-3:]
  smallest_three = sorted_nums[:3]
  m_m  = 1
  for i in largest_three:
    m_m * i
  s_n = smallest_three[0] * smallest_three[1]
  
  return max([s_n * largest_three[-1], m_m])

  

print(maximum_product_of_three([-4, -4, 2, 8]))
print(maximum_product_of_three([98,37,26,48,23,42,64,39,93,50]))