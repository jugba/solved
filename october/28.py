"""Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array of characters with repeats, compress it in place. The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']
Here's a starting point:
"""
import unittest

class Solution(object):
  def compress(self, chars):
    cur = chars[0]
    curr_count = 0
    new_word = []
    for i, val in enumerate(chars):
      if val == cur:
        curr_count += 1
      else:
        new_word.append(cur)
        if curr_count > 1:
          new_word.append(str(curr_count))
        cur = val
        curr_count = 1
    new_word.append(cur)
    if curr_count > 1:
      new_word.append(str(curr_count))
    return new_word

      


class SolutionTest(unittest.TestCase):
  pass
print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'd']))
# ['a', '2', 'b', 'c', '3']
