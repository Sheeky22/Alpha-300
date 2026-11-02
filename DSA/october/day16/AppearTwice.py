class Solution:
    def repeatedCharacter(self, s: str) -> str:
        repeat={}
        for i in s:
            if i in repeat:
                repeat[i]+=1
                if repeat[i]==2:
                    return i
            else:
                repeat[i]=1