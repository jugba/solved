#! /usr/bin/python

"""
Hi, here's your problem today. This problem was recently asked by Apple:

You are given two singly linked lists. The lists intersect at some node. Find, and return the node. Note: the lists are non-cyclical.

Example:

A = 1 -> 2 -> 3 -> 4
B = 6 -> 3 -> 4 

This should return 3 (you may assume that any nodes with the same value are the same node).
"""
import unittest

class Solution:
  def intersection(self, a, b):
    seen = {}
    cur_a = a
    cur_b = b
    while cur_a or cur_b:
      if cur_a:
        if seen.get(cur_a.val):
          return cur_a
        seen[cur_a.val] = 1
        cur_a = cur_a.next
      if cur_b:
        if seen.get(cur_b.val):
          return cur_b
        seen[cur_b.val] = 1
        cur_b = cur_b.next


class SolutionTest(unittest.TestCase):
  def test_intersection(self):
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(6)
    b.next = a.next.next
    s = Solution()
    c = s.intersection(a, b)
    self.assertEqual(c, a.next.next)

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None

  def prettyPrint(self):
    c = self
    while c:
      print(c.val)
      c = c.next

if __name__ == '__main__': 
  unittest.main()