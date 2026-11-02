class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        output = []

        for word in words:
            if len(pattern) != len(word):
                continue

            pattern_to_s = {}
            s_to_pattern = {}
            valid = True

            for a, b in zip(pattern, word):
                if a in pattern_to_s and pattern_to_s[a] != b:
                    valid = False
                    break

                if b in s_to_pattern and s_to_pattern[b] != a:
                    valid = False
                    break

                pattern_to_s[a] = b
                s_to_pattern[b] = a

            if valid:
                output.append(word)

        return output