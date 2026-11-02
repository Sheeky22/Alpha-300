class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern)!=len(s):return False

        pattern_to_s={}
        s_to_pattern={}

        for a,b in zip(pattern,s):
            if a in pattern_to_s and pattern_to_s[a]!=b:
                return False
            
            if b in s_to_pattern and s_to_pattern[b]!=a:
                return False

            pattern_to_s[a]=b
            s_to_pattern[b]=a
        
        return True