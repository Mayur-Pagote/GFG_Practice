class Solution:
    def splitString(ob, S): 
        # code here 
        num_s = ""
        char_s = ""
        spec_s = ""
        for i in S:
            if i.isdigit():
                num_s += i
            elif i.isalpha():
                char_s += i
            else:
                spec_s += i
        return (char_s, num_s, spec_s)
