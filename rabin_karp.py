import numpy as np


def rabin_karp_matcher(text, pattern, radix, prime):
    n = len(text)
    m = len(pattern)
    h = np.power(radix, m - 1) % prime
    p = 0
    t = 0
    for i in range(m):
        p = (radix * p + int(pattern[i])) % prime
        t = (radix * t + int(text[i])) % prime
    for s in range(n - m):  # O(n-m)
        if p == t:
            if pattern == text[s + 1:s + m]:  # O(m) operation
                print("pattern found")
        if s < n - m:
            t = (radix * (t - int(text[s + 1]) * prime)) + int(text[s + m + 1]) % prime


text = "123456758"
pattern = "75"
rabin_karp_matcher(text, pattern, 10, 887)
