class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            encoded_string += str(len(strs[i])) + '#' + strs[i]
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length
            decoded_strings.append(s[start:end])
            i = end
        return decoded_strings