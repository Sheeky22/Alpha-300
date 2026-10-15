class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            a, b = ord(s[l]), ord(s[r])

            if not (48 <= a <= 57 or 65 <= a <= 90 or 97 <= a <= 122):
                l += 1
                continue
            if not (48 <= b <= 57 or 65 <= b <= 90 or 97 <= b <= 122):
                r -= 1
                continue
            if 65 <= a <= 90:
                a += 32
            if 65 <= b <= 90:
                b += 32
            if a != b:
                return False
            l += 1
            r -= 1
        return True