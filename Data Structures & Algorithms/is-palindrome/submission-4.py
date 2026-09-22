class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.replace(" ", "")
        final = new_s.lower()
        valid = set(list("abcdefghjklmnopqrstuvwxyz0123456789"))
        left = 0
        right = len(final)-1
        while right >= left:
            if(final[left] not in valid):
                left+=1
                continue
            if(final[right] not in valid):
                right-=1
                continue
            if(final[left]!=final[right]):
                return False
            left+=1
            right-=1
        return True
        