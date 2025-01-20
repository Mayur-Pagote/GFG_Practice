class Solution:
    def pattern(self, s):
        l = []
        for i in range(len(s), 0, -1):
            l.append(s[:i])
        return l
