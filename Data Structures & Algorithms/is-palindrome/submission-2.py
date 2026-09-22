class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        valid = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))

        new_s = []

        for c in s:
            if c in valid:
                new_s.append(c)

        for i in range(len(new_s)):
            if new_s[i].lower() != new_s[len(new_s)-1-i].lower():
                return False
            
        return True