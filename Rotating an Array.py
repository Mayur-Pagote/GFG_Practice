class Solution:
    def leftRotate(self, arr, d):
        n = len(arr)
        d = d % n
        arr[:] = arr[d:] + arr[:d]  
        return arr

""" 
Time Limit Exceeded
class Solution:
    def leftRotate(self, arr, d):
        # code here
        for i in range(d):
            value = arr.pop(0)
            arr.append(value)
        return arr
"""
