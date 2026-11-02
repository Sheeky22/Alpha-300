class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        start=0
        end=len(s)-1
        vowels=["a","e","i","o","u"]
        while start<end:
            if (s[start].lower() in vowels) & (s[end].lower() in vowels):
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1
            else:
                if s[start].lower() not in vowels:
                    start+=1
                if s[end].lower() not in vowels:
                    end-=1
        return "".join(s)