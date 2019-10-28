#! /usr/bin/python
"""
Hi, here's your problem today. This problem was recently asked by Twitter:

You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

Your solution should run in linear time.

Here's a starting point:
"""
import math
from typing import List

def maximumSum1(a: List[int]) -> int:
  ignored, notignored, res = 0, 0, a[0]
  for num in a:
    if num >= 0:
      ignored += num
      notignored += num
    else:
      ignored = max(ignored + num, notignored)
      notignored += num
        
    res = max([res, ignored if ignored != 0 else -math.inf, notignored if notignored != 0 else -math.inf])
    if ignored < 0: ignored = 0
    if notignored < 0: notignored = 0
  return max(res, max(a))

print(maximumSum1([11,-10,-11,8,7,-6,9,4,11,6,5,0]))

def maximumSum(arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        size = len(arr)
        if size == 0:
            return 0
        max_sum = arr[0]
        curr_max = arr[0]
        
        dele = None
        has_rem = False
        
        for i in range(1, size):
            curr_max += arr[i]
            if not has_rem and arr[i] < 0:
                curr_max -= arr[i]
                has_rem = True
                dele = arr[i]
            elif has_rem and arr[i] < 0 and arr[i] < dele:
                curr_max += dele
                curr_max -= arr[i] 
                dele = arr[i]

            if curr_max < arr[i]:
                curr_max = arr[i]
                has_rem = None
            if curr_max > max_sum:
                max_sum = curr_max
        return max_sum

# maximumSum([8,-1,6,-7,-4,5,-4,7,-6])
maximumSum([11,-10,-11,8,7,-6,9,4,11,6,5,0])


def max_subarray_sum(arr):
  size = len(arr)
  if size == 0:
    return 0
  max_sum = arr[0]
  curr_max = arr[0]

  for i in range(1, size):
    curr_max += arr[i]
    if curr_max > max_sum:
      max_sum = curr_max
    if curr_max < arr[i]:
      curr_max = arr[i]
  return max_sum
    
  

# print( max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
