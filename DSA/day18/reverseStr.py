class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        start=0
        end=0
        while start<len(s):
            while end<len(s):
                if s[end]==" ":
                    break
                else:
                    end+=1
            left=start
            right=end-1
            while left<right:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            start=end+1
            end+=1
        return "".join(s)
                