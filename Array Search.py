class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        if x in arr:
            return arr.index(x)
        return -1
