class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False

        double=s+s
        n=len(s)
        i=0
        while i<n:
            for j in range(len(s)):
                if goal[j]!=double[i+j]:
                    break
            else:
                return True
            i+=1
        return False