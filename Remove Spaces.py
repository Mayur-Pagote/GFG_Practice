class Solution:
    def modify(self, s):
        # code here
        S = " "
        for i in s:
            if i == " ":
                continue
            else:
                S += i
        return S
