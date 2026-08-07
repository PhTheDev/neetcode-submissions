from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        contagem = dict(Counter(s))
        odd_freqs = [f for f in contagem.values() if f % 2 != 0]
        even_freqs = [f for f in contagem.values() if f % 2 == 0]
        return max(odd_freqs) - min(even_freqs)