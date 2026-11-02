class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        i = len(s) - 1

        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1

            if i < 0:
                break

            j = i
            while i >= 0 and s[i] != ' ':
                i -= 1

            for k in range(i + 1, j + 1):
                result.append(s[k])
            result.append(' ')
        if result:
            result.pop()

        return ''.join(result)

        