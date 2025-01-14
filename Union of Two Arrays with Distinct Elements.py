class Solution:
    def findUnion(self, a, b):
        union_set = set(a) | set(b)  
        return sorted(union_set)  

"""
Time Limit Exceeded
class Solution:
    def findUnion(self,a, b):
        #Your code here
        l = []
        for i in a:
            if i not in l:
                l.append(i)
        for j in b:
            if j not in l:
                l.append(j)
        l.sort()
        return l
"""
