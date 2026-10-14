class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        commonChar = {}
        for ch in words[0]:
            commonChar[ch] = commonChar.get(ch, 0) + 1

        for word in words[1:]:
            currentChar = {}
            for ch in word:
                currentChar[ch] = currentChar.get(ch, 0) + 1
            for ch in list(commonChar.keys()):
                commonChar[ch] = min(
                    commonChar[ch],
                    currentChar.get(ch, 0)
                )
                if commonChar[ch] == 0:
                    del commonChar[ch]
        result = []
        for ch, freq in commonChar.items():
            for _ in range(freq):
                result.append(ch)
        return result