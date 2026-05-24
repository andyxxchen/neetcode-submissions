class Solution:
    def is_alchar(self, c: str) -> bool:
        if (c.lower() >= 'a' and c.lower() <= 'z') or (c.lower() >= '0' and c.lower() <= '9'):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i <= j:
            while i < len(s) and not self.is_alchar(s[i]):
                i += 1
            while j >= 0 and not self.is_alchar(s[j]):
                j -= 1
            
            if i<len(s) and j >= 0 and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

