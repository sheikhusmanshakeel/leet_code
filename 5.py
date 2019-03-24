# https://leetcode.com/problems/longest-palindromic-substring/


def longest_palindrome_substring_bf(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j] == s[1:j][::-1] and j - i >= len(longest):
                longest = s[i:j]
    return longest


def longest_palindrome_better(s):
    start = 0
    end = 0
    for i in range(len(s)):
        left, right = helper(s, i, i)
        if right - left > end - start:
            start = left
            end = right
        left, right = helper(s, i, i + 1)
        if right - left > end - start:
            start = left
            end = right

    return s[start:end + 1]


def helper(s, left, right):
    if right >= len(s):
        return 0, 0
    start = left
    end = right
    while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1

    return start + 1, end - 1


print(longest_palindrome_substring_bf("babad"))
