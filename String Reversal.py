class Solution:
    def reverseString(self, s):
        # code here
        S = ""
        for i in s[::-1]:
            if i == " ":
                continue
            if i not in S:
                S += i
        return S
