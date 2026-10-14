class Solution:    
    def findUnion(self, a, b):
        sol=[]
        dups={}
        for i in a:
            if i not in dups:
                sol.append(i)
                dups[i]=True
        for i in b:
            if i not in dups:
                sol.append(i)
                dups[i]=True
        return sol