class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(len(s)):
            left, right = self.helper(s, i, i)
            if right - left > end - start:
                start = left
                end = right
            left, right = self.helper(s, i, i + 1)
            if right - left > end - start:
                start = left
                end = right

        return s[start:end + 1]

    def helper(self, s, left, right):
        if right >= len(s):
            return 0, 0
        start = left
        end = right
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

        return start + 1, end - 1


print(Solution().longestPalindrome("babad"))
