class Solution(object):
    def isPalindrome(self, s):
        ans = ""

        for ch in s:
            if ch.isalnum():
                ans += ch.lower()

        return ans == ans[::-1]