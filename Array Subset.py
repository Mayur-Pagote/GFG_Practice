class Solution:
    # Function to check if b is a subset of a.
    def isSubset(self, a, b):
        # Converting list a to a set for faster lookups.
        set_a = set(a)
        
        # Check if all elements in b are present in set_a.
        for element in b:
            if element not in set_a:
                return False
        return True
