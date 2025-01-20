class Solution:
    def count (self,s):
        # your code here
        u_char = 0
        l_char = 0
        s_char = 0
        n_char = 0
        for i in s:
            if i.isdigit():
                n_char += 1
            elif i.isupper():
                u_char += 1
            elif i.islower():
                l_char += 1
            else:
                s_char += 1
        return (u_char, l_char, n_char, s_char)
