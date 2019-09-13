#! /usr/bin/python
"""
You are given an array. Each element represents the price of a stock on that particular day. Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).

Here's your starting point:

def buy_and_sell(arr):
  #Fill this in.
  
print buy_and_sell([9, 11, 8, 5, 7, 10])
"""

import unittest

class Solution:
  def buy_and_sell(self, ticks):
    size =  len(ticks)
    smallest = ticks[0]
    optimal_sell = None
    optimal_buy = None

    m_profit = float('-inf')
    for i in range(size):
     if i > 0:
        tm = ticks[i] - smallest
        if tm > m_profit:
          m_profit = tm
          optimal_sell = ticks[i]
          optimal_buy = smallest

        if ticks[i] < smallest:
          smallest = ticks[i]
    return optimal_buy

        
         



class SolutionTest(unittest.TestCase):

  def test_buy_sell(self):
    s = Solution()
    ans = s.buy_and_sell([9, 11, 8, 18, 5, 7, 10])
    self.assertEqual(ans, 8)

if __name__ == '__main__':
  unittest.main()
    