class Solution:
    def sort(self, s): 
        #code here
        S = ""
        s = list(s)
        s.sort()
        for i in s:
            S += i
        return S
