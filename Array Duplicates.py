class Solution:
    def findDuplicates(self, arr):
        
        seen = set()
        duplicates = []

        for num in arr:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)

        return duplicates



""" 
Time Limit Exceeded
class Solution:
    def findDuplicates(self, arr):
        # code here
        l = []
        s = set(arr)
        for i in s:
            if arr.count(i) > 1:
                l.append(i)
        return l
"""
