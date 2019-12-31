# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def longest_substring(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    seen = dict()
    longest_length = 0
    for c in s:
        if seen.__contains__(c):
            if longest_length < len(seen):
                longest_length = len(seen)
            seen = {c: c}  # This is the problem here. I am losing the entire dictionary
        else:
            seen[c] = c
    return longest_length


def other_solution(s):
    start = max_length = 0
    seen = {}

    for i in range(len(s)):
        if s[i] in seen and start <= seen[s[i]]:
            start = seen[s[i]] + 1
        else:
            new_length = i - start + 1
            max_length = max(max_length, new_length)

        seen[s[i]] = i

    return max_length


print(other_solution("usman shakeel l"))
print(longest_substring("    "))
print(longest_substring("0"))
print(longest_substring(" abc abcbb  "))
print(longest_substring("pwwkew"))
print(longest_substring("abcabcbb"))
print(longest_substring("bbbbbbbb"))
