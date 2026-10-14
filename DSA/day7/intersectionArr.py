class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashMap={}
        res=[]
        for i in nums1:
            if i not in hashMap:
                hashMap[i]=True
        for i in nums2:
            if i in hashMap:
                res.append(i)
                del hashMap[i]
        return res