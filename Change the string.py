class Solution:
    def modify(self, s):
        if s[0].isupper():
            return s.upper()
        else:
            return s.lower()
