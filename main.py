
"""
Hi, here's your problem today. This problem was recently asked by Uber:

Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 5^2 + 12^2 = 13^2.

"""

def findPythagoreanTriplets(nums):
  A = {}
  size = len(nums)
  for i in range(size):
    p = nums[i] ** 2
    A[p] = 1
    nums[i] = p

  for i, val in enumerate(nums):
    j = i + 1
    while j < size:
      t = nums[i] + nums[j]
      if A.get(t):
        return True
      j += 1

  return False

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True