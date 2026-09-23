class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        largest = 0
        max_freq = 0
        characterCounter = {}
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            characterCounter[letter] = 0

        while right < len(s):
            characterCounter[s[right]] += 1
            max_freq = max(max_freq, characterCounter[s[right]])

            length = right - left + 1

            if length - max_freq > k:
                characterCounter[s[left]] -= 1
                left += 1
            else:
                if largest < length:
                    largest = length
            
            right += 1

        return largest