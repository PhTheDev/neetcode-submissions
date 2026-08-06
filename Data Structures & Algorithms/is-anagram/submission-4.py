class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sOrdenada = sorted(s)
        tOrdenada = sorted(t)
        if sOrdenada == tOrdenada:
            return True
        else: return False