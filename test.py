#! /urs/bin/python

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        M = {}
        b = 'balloon'
        B = {}
        for a in b:
            B[a] = B[a] if B.get(a) else 0
            B[a] += 1
    
        for i in text:
            M[i] = M[i] if M.get(i) and i in B else 1
            M[i] += 1
        t = 0
        final = {}
        for key, value in B.items():
            if M.get(key):
                t =  M[key]//value
                final[key] = t
            else:
                return 0
        return min(final.keys())

s = Solution()
s.maxNumberOfBalloons("loonbalxballpoon")
