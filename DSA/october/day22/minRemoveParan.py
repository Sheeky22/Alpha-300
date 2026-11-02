class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res=[]
        count=0

        for i in s:
            if i=="(":
                res.append(i)
                count+=1
            elif i==")" and count>0:
                res.append(i)
                count-=1
            elif i!=")":
                res.append(i)
        
        finalRes=[]
        for j in res[::-1]:
            if j=="(" and count>0:
                count-=1
            else:
                finalRes.append(j)
        return "".join(finalRes[::-1])