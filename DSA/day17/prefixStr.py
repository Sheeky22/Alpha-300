class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentenceList = sentence.split()

        for i in range(len(sentenceList)):
            for j in range(len(searchWord)):
                if j >= len(sentenceList[i]) or sentenceList[i][j] != searchWord[j]:
                    break
            else:
                return i + 1

        return -1