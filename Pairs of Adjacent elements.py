class Solution:
    def adjacentPairs(self,arr):
        # code here
        count = 0
        for i in range(len(arr)-1):
            if arr[i]+1 == arr[i+1]:
                count += 1
        return count
