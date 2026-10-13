class Solution:
    def missingNum(self, arr):
        # code here
        sums=0
        for i in range(len(arr)+1):
            sums^=i+1
            if i==len(arr):
                break
            sums^=arr[i]
        return sums