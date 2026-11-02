class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        result=[]

        for i in s:
            if i==")":
                count-=1
            if count!=0:
                result.append(i)
            if i=="(":
                count+=1
        return "".join(result)
        