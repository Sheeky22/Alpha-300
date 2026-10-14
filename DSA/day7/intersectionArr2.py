class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashMap={}
        res=[]
        for i in nums1:
            if i not in hashMap:
                hashMap[i]=1
            else:
                hashMap[i]+=1
        for i in nums2:
            if i in hashMap:
                res.append(i)
                hashMap[i]-=1
                if hashMap[i]==0:
                    del hashMap[i]
        return res