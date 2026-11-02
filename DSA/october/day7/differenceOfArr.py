class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        hashMap1={}
        hashMap2={}
        ans=[[],[]]
        for i in nums1:
           if i not in hashMap1:
                hashMap1[i]=True
        for i in nums2:
           if i not in hashMap2:
                hashMap2[i]=True 
        for i in nums1:
           if i not in hashMap2:
                ans[0].append(i)
                hashMap2[i]=True
        for i in nums2:
           if i not in hashMap1:
                ans[1].append(i)
                hashMap1[i]=True   
        return ans