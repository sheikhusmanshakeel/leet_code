

# implement an algorithm to determine if a string has all unique characters without using additional data structures

def is_unique(s):
    for n in range(len(s)-1):
        for x in s[n+1:]:
            if x == s[n]:
                # duplicate found
                return False

    return True


s1 = "abcdac"
ret1 = False
assert is_unique(s1) == ret1

s2 = "abcdef"
ret2 = True
assert is_unique(s2) == ret2