class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        # code here
        x = int(len(arr) / 2)
        left = arr[:x]
        right = arr[x:]
        res = sum(left) - sum(right)
        return abs(res)
