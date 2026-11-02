class Solution:
    def toLowerCase(self, s: str) -> str:
        res=[]
        for i in s:
            if i.islower():
                res.append(i)
            else:
                res.append(i.lower())
        return "".join(res)