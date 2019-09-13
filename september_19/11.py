#! /usr/bin/python

"""
You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted,
and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

Here's a starting point:

def merge(intervals):
  # Fill this in.
  
print merge([(1, 3), (5, 8), (4, 10), (20, 25)])
# [(1, 3), (4, 10), (20, 25)]
"""
import unittest

class Solution():
  def merge(self, intervals):
    intervals = sorted(intervals, key=lambda k:k[0])
    size = len(intervals)
    new_arr = []
    for i in range(size):
      if i == 0:
        new_arr.append(intervals[0])
        continue
      pre = intervals[i-1]
      cur = intervals[i]
      if pre[1] > cur[1] and pre[0] < cur[0]:
        intervals[i] = pre
      else:
        new_arr.append(cur)
    return new_arr


class SolutionTest(unittest.TestCase):
  def test_merge(self):
    s = Solution()
    ans = s.merge([(1, 3),(0, 4), (5, 8), (4, 10), (20, 25)])
    self.assertEqual(ans, [(0, 4), (4, 10), (20, 25)])
    ans = s.merge([(1, 3), (5, 8), (4, 10), (20, 25)])
    self.assertEqual(ans, [(1, 3), (4, 10), (20, 25)] )

if __name__ == '__main__':
  unittest.main()