class Solution:
    def gameResult(self, s):
        # code here
        if s[0] == s[-1]:
            return "DRAW"
        elif s[0] == "R" and s[-1]=="S":
            return "A"
        elif s[0] == "P" and s[-1] == "R":
            return "A"
        elif s[0] == "S" and s[-1] == "P":
            return "A"
        else:
            return "B"
