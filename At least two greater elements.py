class Solution:
    def findElements(self,arr):
        # Your code goes here
        for i in range(2):
            val1 = max(arr)
            arr.remove(val1)
        
        arr.sort()
        return arr
