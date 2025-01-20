class Solution:
    def solve(self, a):
        # code here
        l = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
        set_c = set()
        for i in a:
            if i in l:
                continue
            else:
                set_c.add(i)
        if len(set_c) % 2 == 0:
            return "SHE!"
        else:
            return "HE!"
