class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(ch.lower() for ch in s if ch.isalnum())
        p, q = 0, len(clean_s) - 1
        while p < q:
            if clean_s[p] != clean_s[q]:
                break
            p += 1
            q -= 1
        if p < q:
            return False
        else:
            return True