class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}

        for i in strs:
            charFreq=[0]*26
            for j in i:
                charFreq[ord(j)-ord('a')]+=1
            if tuple(charFreq) in anagram:
                anagram[tuple(charFreq)].append(i)
            else:
                anagram[tuple(charFreq)]=[i]
        return list(anagram.values())
        
        