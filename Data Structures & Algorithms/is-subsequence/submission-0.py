class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        for letra in t:
            if i < len(s) and letra == s[i]:
                i += 1
        if i == len(s):
            return True
        else:
            return False