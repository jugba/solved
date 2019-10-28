#! /usr/bin/python
"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

import unittest

class Solution():
    def take2(self, A):
        start = 0
        end = len(A)
        counter = 0
        n = None
        while start < len(A):
            if A[start] == 0:
                if n is not None:
                    nex = n + 1
                else:
                    nex = start + 1
                while nex < end:
                    counter += 1
                    if A[nex] != 0:
                        A[start], A[nex] = A[nex], A[start]
                        break
                    nex += 1
                    n = nex
            start += 1
        print('final number of operations', counter)

    def moveZeros(self, A):
        next_zero, none_zero = 0, len(A) - 1
        while next_zero < none_zero:
            if A[next_zero] != 0:
                next_zero += 1
            else:
                A[next_zero], A[none_zero] = A[none_zero], A[next_zero]
                none_zero -= 1
        start, end = 0, none_zero-1
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        A = []
        self.solution.moveZeros(A)
        self.assertEqual(A, [])
    
    def test_none_empty_list(self):
        A = [0, 0, 0, 2, 0, 1, 0, 3, 4, 0, 0]
        self.solution.take2(A)
        self.assertEqual(A, [2, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0])

        B = [0,1,0,3,12]
        self.solution.take2(B)
        self.assertEqual(B, [1,3,12,0,0])

if __name__ == '__main__':
    unittest.main()

# b = [0, 0, 0, 2, 0, 1, 0, 3, 4, 0, 0]
# moveZeros(b)
# print(b)
