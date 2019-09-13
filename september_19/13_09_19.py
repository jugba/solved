"""
Implement a queue class using two stacks. 
A queue is a data structure that supports the FIFO protocol (First in = first out). 
Your class should support the enqueue and dequeue methods like a standard queue.
"""

import unittest
class Queue:
  def __init__(self):
    self.in_stack = []
    self.out_stack = []
    
  def enqueue(self, val):
    self.in_stack.append(val)

  def dequeue(self):
    if len(self.out_stack) == 0:
      if len(self.in_stack) == 0:
        return None
      else:
        while self.in_stack:
          ele = self.in_stack.pop()
          self.out_stack.append(ele)
    return self.out_stack.pop()

class QueueTest(unittest.TestCase):
  def setUp(self):
    self.Q = Queue()
  
  def test_empty_dequeue(self):
    self.assertEqual(self.Q.dequeue(), None)
  
  def test_non_empty_queue(self):
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    self.assertEqual(q.dequeue(), 1)
    self.assertEqual(q.dequeue(), 2)
    self.assertEqual(q.dequeue(), 3)
    self.assertEqual(q.dequeue(), None)



if __name__ == '__main__':
  unittest.main()