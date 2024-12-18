class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, arr1, arr2) -> bool:
        #code here
        arr1.sort()
        arr2.sort()
        return arr1==arr2
